# ruff: noqa: PLR2004, PLR0912, PLR0915, N802
"""
Module based on the HTML translators from sphinx and docutils.

The code in this module contains very little new code. Most of it has been
copied from docutils and sphinx repositories at specific commits. The
functionality of sphinx-colorschemed-images could have been implemented with
relatively little code, but it would only have worked under a very specific
combination of docutils and Sphinx. In order to make the extension work in
other Sphinx projects, code from docutils and sphinx had to be copied here.

Thanks to tox, the battery of tests of this extension can be executed against
different versions of Sphinx to verify that the extension works as expected.

Here is the correspondence between the functions in this module and
their origin (using docutils at commit ceb8eb76a and sphinx at 8042eb633):

 * parse_measure         <- docutils.nodes
 * amend_attributes      <- sphinx.writers.html5.HTML5Translator.visit_image

From docutils.writers._html_base.HTMLTranslator methods:
 * CS_read_size_with_PIL <- read_size_with_PIL
 * CS_image_size         <- image_size
 * CS_visit_image        <- visit_image
"""
import base64
import mimetypes
import numbers
import posixpath
import re
import urllib.parse
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst.directives.images import PIL
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.images import get_image_size

logger = logging.getLogger(__name__)


def parse_measure(measure: str) -> tuple[numbers.Rational, str]:
    """Parse a measure__, return value + optional unit.

    __ https://docutils.sourceforge.io/docs/ref/doctree.html#measure

    Provisional.
    """
    match = re.fullmatch("(-?[0-9.]+) *([a-zA-Zµ]*|%?)", measure)
    try:
        try:
            value = int(match.group(1))
        except ValueError:  # pragma: no cover
            value = float(match.group(1))
        unit = match.group(2)
    except (AttributeError, ValueError) as exc:  # pragma: no cover
        raise ValueError(f'"{measure}" is no valid measure.') from exc
    return value, unit


def visit_colorschemed_image(self, node):
    # pragma: no cover
    def CS_read_size_with_PIL(node):  # pragma: no cover
        # Try reading size from image file.
        # Internal auxiliary method called from `self.image_size()`.
        reading_problems = []
        uri = node["uri"]
        if not PIL:
            reading_problems.append("Requires Python Imaging Library.")
        if mimetypes.guess_type(uri)[0] in self.videotypes:
            reading_problems.append("PIL cannot read video images.")
        if not self.settings.file_insertion_enabled:
            reading_problems.append("Reading external files disabled.")
        if not reading_problems:
            try:
                imagepath = self.uri2imagepath(uri)
                with PIL.Image.open(imagepath) as img:
                    imgsize = img.size
            except (ValueError, OSError, UnicodeEncodeError) as err:
                reading_problems.append(str(err))
            else:
                self.settings.record_dependencies.add(imagepath)
        if reading_problems:
            msg = [
                "Cannot scale image!",
                f'Could not get size from "{uri}":',
                *reading_problems,
            ]
            self.messages.append(
                self.document.reporter.warning("\n  ".join(msg), base_node=node)
            )
            return None
        return imgsize

    def CS_image_size(node: nodes.image) -> dict[str, str]:
        """Determine the image size from node arguments or the image file.

        Return as dictionary of <img> attributes,
        e.g., ``{height': '32', 'style': 'width: 4 em;'}``.

        Auxiliary method called from `self.visit_image()`.
        Provisional.
        """
        dimensions = ("width", "height")
        measures = {}  # (value, unit)-tuples) for width and height
        for dimension in dimensions:
            if dimension in node:
                measures[dimension] = parse_measure(node[dimension])
        if "scale" in node and len(measures) < 2:  # pragma: no cover
            # supplement with (unitless) values read from image file
            imgsize = self.read_size_with_PIL(node)
            if imgsize:
                for dimension, value in zip(dimensions, imgsize):
                    if dimension not in measures:
                        measures[dimension] = (value, "")
        # Scale and format as <img> attributes,
        # use "width" and "hight" for unitless values and "style" else:
        scaling_factor = node.get("scale", 100) / 100
        size_atts = {}
        declarations = []  # declarations for the "style" attribute
        for dimension, (value, unit) in measures.items():
            value *= scaling_factor  # noqa: PLW2901
            if unit:  # pragma: no cover
                declarations.append(f"{dimension}: {value:g}{unit};")
            else:
                size_atts[dimension] = f"{round(value)}"
        if declarations:  # pragma: no cover
            size_atts["style"] = " ".join(declarations)

        # This is the specific part of colorschemed_images. To pass the
        # data attributes that hold the alternative src url for the images,
        # for each color-scheme.
        data_attrs = [
            attr
            for attr in node.attributes
            if attr.startswith("data-alt-src-color-scheme")
        ]
        for data_attr in data_attrs:
            filename = Path(node[data_attr]).name
            size_atts[data_attr] = Path(self.builder.imgpath) / filename

        return size_atts

    # This method is taken from ``sphinx.writers.html5.HTML5Translator``
    # class, method ``visit_image``.
    def amend_attributes(node):
        olduri = node["uri"]
        # rewrite the URI if the environment knows about it
        if olduri in self.builder.images:
            node["uri"] = posixpath.join(
                self.builder.imgpath,
                urllib.parse.quote(self.builder.images[olduri]),
            )

        if "scale" in node:  # pragma: no cover  # noqa: SIM102
            # Try to figure out image height and width.  Docutils does that
            # too, but it tries the final file name, which does not
            # necessarily exist yet at the time the HTML file is written.
            if not ("width" in node and "height" in node):
                path = str(Path(self.builder.srcdir) / olduri)
                size = get_image_size(path)
                if size is None:
                    logger.warning(
                        __(
                            "Could not obtain image size. :scale: "
                            "option is ignored."
                        ),
                        location=node,
                    )
                else:
                    if "width" not in node:
                        node["width"] = str(size[0])
                    if "height" not in node:
                        node["height"] = str(size[1])

    def CS_visit_image(node):
        # First, fix uri, and try to add width and height to the node.
        self.amend_attributes(node)
        uri = node["uri"]
        alt = node.get("alt", uri)
        mimetype = mimetypes.guess_type(uri)[0]
        element = ""  # The HTML element (including potential children).
        # Attributes for the HTML tag:
        atts = self.image_size(node)
        if "align" in node:  # Alignment is handled by CSS rules.
            atts["classes"] = [f"align-{node['align']}"]
        # ``:loading:`` option (embed, link, lazy), default from setting,
        # exception: only embed videos if told via directive option.
        loading = "link" if mimetype in self.videotypes else self.image_loading
        loading = node.get("loading", loading)
        if loading == "lazy":  # pragma: no cover
            atts["loading"] = "lazy"
        elif loading == "embed":  # pragma: no cover
            try:
                imagepath = self.uri2imagepath(uri)
                if mimetype == "image/svg+xml":
                    imagedata = Path(imagepath).read_text(encoding="utf-8")
                else:
                    imagedata = Path(imagepath).read_bytes()
            except (ValueError, OSError, UnicodeError) as err:
                self.messages.append(
                    self.document.reporter.error(
                        f'Cannot embed image "{uri}":\n {err}', base_node=node
                    )
                )
            else:
                self.settings.record_dependencies.add(imagepath)
                if mimetype == "image/svg+xml":
                    element = self.prepare_svg(imagedata, node, atts)
                else:
                    data64 = base64.b64encode(imagedata).decode()
                    uri = f"data:{mimetype};base64,{data64}"

        # No newlines around inline images (but all images may be nested
        # in a `reference` node which is a `TextElement` instance):
        if (
            not isinstance(node.parent, nodes.TextElement)
            or isinstance(node.parent, nodes.reference)
            and not isinstance(node.parent.parent, nodes.TextElement)
        ):
            suffix = "\n"
        else:
            suffix = ""  # pragma: no cover

        if mimetype in self.videotypes:  # pragma: no cover
            atts["title"] = alt
            if "controls" in node["classes"]:
                node["classes"].remove("controls")
                atts["controls"] = "controls"
            element = (
                self.starttag(node, "video", suffix, src=uri, **atts)
                + f'<a href="{node["uri"]}">{alt}</a>{suffix}'
                + f"</video>{suffix}"
            )
        elif mimetype == "application/x-shockwave-flash":  # pragma: no cover
            atts["type"] = mimetype
            element = (
                self.starttag(node, "object", "", data=uri, **atts)
                + f"{alt}</object>{suffix}"
            )
        elif element:  # embedded SVG, see above
            element += suffix  # pragma: no cover
        else:
            atts["alt"] = alt
            element = self.emptytag(node, "img", suffix, src=uri, **atts)
        self.body.append(element)
        if suffix:  # block-element
            self.report_messages(node)

    # -----------------------------------------------------
    if not getattr(self, "_overwritten__read_size_with_PIL", None):
        if getattr(self, "read_size_with_PIL", None):
            self._overwritten__read_size_with_PIL = self.read_size_with_PIL
        self.read_size_with_PIL = CS_read_size_with_PIL

    if not getattr(self, "_overwritten__image_size", None):
        if getattr(self, "image_size", None):
            self._overwritten__image_size = self.image_size
        self.image_size = CS_image_size

    if not getattr(self, "amend_attributes", None):
        self.amend_attributes = amend_attributes

    if not getattr(self, "_overwritten__visit_image", None):
        if getattr(self, "visit_image", None):
            self._overwritten__visit_image = self.visit_image
        self.visit_image = CS_visit_image

    self.visit_image(node)

    if getattr(self, "_overwritten__read_size_with_PIL", None):
        self.read_size_with_PIL = self._overwritten__read_size_with_PIL
        delattr(self, "_overwritten__read_size_with_PIL")

    if getattr(self, "_overwritten__image_size", None):
        self.image_size = self._overwritten__image_size
        delattr(self, "_overwritten__image_size")

    if getattr(self, "_overwritten__visit_image", None):
        self.visit_image = self._overwritten__visit_image
        delattr(self, "_overwritten__visit_image")


def depart_colorschemed_image(self, node):
    pass
