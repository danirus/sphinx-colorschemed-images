import os
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst.directives.images import Figure, Image
from docutils.utils import relative_path
from sphinx.environment.adapters.asset import ImageAdapter
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.display import status_iterator
from sphinx.util.images import guess_mimetype
from sphinx.util.osutil import copyfile, ensuredir

from .exceptions import CSIExtensionError
from .translator import depart_colorschemed_image, visit_colorschemed_image

logger = logging.getLogger(__name__)


class colorschemed_image(nodes.image):  # noqa: N801
    pass


class ColorschemedMixin:
    """Shared method between ``image`` and ``figure`` directives."""

    def replace_image_node(self, node, image_paths):
        options = node.attributes
        config = self.env.app.config
        default_color_scheme = config.csi_default_color_scheme

        for color_scheme, img_path in image_paths.items():
            options[f"data-alt-src-color-scheme-{color_scheme}"] = img_path

        parent = Path(options["uri"]).parent
        filename = Path(image_paths.get(default_color_scheme)).name
        options["uri"] = str(parent / filename)
        return colorschemed_image(node.rawsource, **options)


class ColorschemedImage(Image, ColorschemedMixin):
    """Implements the cs_image directive."""

    def run(self):
        self.env = self.state.document.settings.env

        result = []
        parent = super().run()
        for node in parent:
            if isinstance(node, nodes.image):
                image_paths = get_image_paths(self.env, node)
                if len(image_paths) > 0:
                    _node = self.replace_image_node(node, image_paths)
                    result.append(_node)
                else:
                    result.append(node)
        return result


class ColorschemedFigure(Figure, ColorschemedMixin):
    """Implements the cs_figure directive."""

    def run(self):
        self.env = self.state.document.settings.env

        result = []
        origin = super().run()
        for node in origin:
            if isinstance(node, nodes.figure):
                children = []
                for cnode in node.children:
                    if isinstance(cnode, nodes.image):
                        img_pths = get_image_paths(self.env, cnode)
                        if len(img_pths) > 0:
                            _node = self.replace_image_node(cnode, img_pths)
                            _node.parent = cnode.parent
                            children.append(_node)
                        else:
                            children.append(cnode)
                    else:
                        children.append(cnode)
                node.children = children
            result.append(node)

        return result


def get_image_paths(env, node):
    existing_img_paths = {}
    calculated_img_paths = {}
    node_uri = Path(node["uri"])
    try:
        for color_scheme in env.app.config.csi_color_schemes:
            img_path = env.app.config.csi_image_path_pattern.format(
                root=str(node_uri.parent / node_uri.stem),
                ext=node_uri.suffix,
                path=str(node_uri.parent),
                basename=node_uri.stem,
                docpath=str(Path(env.docname)),
                language=env.app.config.language,
                colorscheme=color_scheme,
            )
            calculated_img_paths[color_scheme] = img_path
            _, full_img_path = env.relfn2path(img_path, env.docname)
            candidates = collect_candidates(env.app, full_img_path, node)

            for img_path in candidates.values():
                full_img_path = str(Path(env.app.srcdir) / img_path)
                if not os.access(full_img_path, os.R_OK):  # pragma: no cover
                    logger.warning(
                        __("image file not readable: %s"),
                        img_path,
                        location=node,
                        type="image",
                        subtype="not_readable",
                    )
                    continue
                existing_img_paths[color_scheme] = img_path

    except KeyError as exc:
        msg = (
            'Invalid csi_image_path_pattern: "'
            f'{env.app.config.csi_image_path_pattern}" - {exc!r}'
        )
        raise CSIExtensionError(msg) from exc

    if not hasattr(env, "colorschemed_images"):
        env.colorschemed_images = []

    for color_scheme, img_path in existing_img_paths.items():
        if color_scheme != env.app.config.csi_default_color_scheme:
            env.colorschemed_images.append((img_path, Path(img_path).name))

    if len(existing_img_paths) < len(calculated_img_paths):
        not_found = [
            k for k in calculated_img_paths if k not in existing_img_paths
        ]
        for k in not_found:
            logger.warning(
                __("image not found: %s"),
                calculated_img_paths[k],
                location=node,
            )

    return existing_img_paths


# This function is almost identical to the method 'collect_candidates'
# in sphinx/environment/collectors/asset.py::ImageCollector class.
def collect_candidates(env, img_path, node):
    globbed = {}
    candidates = {}
    img_path = Path(img_path)
    for filename in img_path.parent.glob(img_path.name):
        new_img_path = relative_path(str(Path(env.srcdir) / "dummy"), filename)
        try:
            mimetype = guess_mimetype(filename)
            if mimetype is None:  # pragma: no cover
                suffix = Path(filename).suffix
                mimetype = "image/x-" + suffix[1:]
            if mimetype not in candidates:
                globbed.setdefault(mimetype, []).append(new_img_path)
        except OSError as err:  # pragma: no cover
            logger.warning(
                __("image file %s not readable: %s"),
                filename,
                err,
                location=node,
                type="image",
                subtype="not_readable",
            )

    for key, files in globbed.items():
        candidates[key] = min(files, key=len)  # select by similarity

    return candidates


def copy_colorschemed_images(app, *args):
    """Copy colorschemed_images that were not copied by the HTML Builder."""
    if not hasattr(app.env, "colorschemed_images"):
        return

    images = dict(app.env.colorschemed_images)
    images_dir = Path(app.builder.imagedir)
    ensuredir(images_dir)
    stringify_func = ImageAdapter(app.env).get_original_image_uri

    for src in status_iterator(
        images,
        __("copying colorschemed_images... "),
        "brown",
        len(images),
        app.verbosity,
        stringify_func=stringify_func,
    ):
        # import ipdb; ipdb.set_trace()
        dest = images[src]
        try:
            copyfile(
                app.srcdir / src, app.outdir / images_dir / dest, force=True
            )
        except Exception as err:  # pragma: no cover
            logger.warning(
                __("cannot copy image file '%s': %s"), app.srcdir / src, err
            )


# ---------------------------------------------------------------------
def extension_builder_inited(app):
    app.config.html_static_path.append(
        str(Path(__file__).parent.joinpath("static").absolute())
    )
    app.add_node(
        colorschemed_image,
        html=(visit_colorschemed_image, depart_colorschemed_image),
    )
    app.add_directive("cs_image", ColorschemedImage)
    app.add_directive("cs_figure", ColorschemedFigure)

    # Assert that the setting csi_default_color_scheme, given by the user
    # in the conf.py, is also part of the list of color schemes given by
    # the user in the setting csi_color_schemes. Raise otherwise.
    #
    # include_js_script = app.env.config.csi_include_js_script
    default_color_scheme = app.env.config.csi_default_color_scheme
    color_schemes = app.env.config.csi_color_schemes

    if app.config.csi_add_script_to_html_output:
        app.add_js_file("sphinx-colorschemed-images.js")

    if default_color_scheme not in color_schemes:
        raise CSIExtensionError(
            f"Setting hl(csi_default_color_scheme) '{default_color_scheme}' is"
            f" not contained in setting hl(csi_color_schemes) {color_schemes}."
        )
