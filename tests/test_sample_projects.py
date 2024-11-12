from pathlib import Path

import pytest
from lxml import etree
from sphinx.errors import ExtensionError

from sphinx_colorschemed_images.exceptions import CSIExtensionError


# ---------------------------------------------------------------------
def test_prj1_fails_to_build(test_app):
    """
    Test that the project fails to build, because of wrong settings.

    Specifically, the setting csi_default_color_scheme is not listed in the
    setting csi_color_schemes. And that is wrong. When those two settings are
    not given, the ``csi_default_color_scheme`` is ``'light'`` and the setting
    ``csi_color_schemes`` is ``['light', 'dark']``.
    """
    with pytest.raises(ExtensionError) as excinfo:
        test_app(buildername="html", srcdir="sample_prj_1")

    assert isinstance(excinfo.value.orig_exc, CSIExtensionError)
    assert excinfo.value.orig_exc.args[0] == (
        "Setting \x1b[34mcsi_default_color_scheme\x1b[0m 'unknown' is "
        "not contained in setting \x1b[34mcsi_color_schemes\x1b[0m ['light', "
        "'dark']."
    )


# ---------------------------------------------------------------------
# Sample Project 2 tests.


def test_prj2_builds_successfully(sample_prj2):
    """Test that the project has built without problems."""
    index = Path(sample_prj2.outdir, "index.html").read_text()
    assert "Sample Project 2" in index


# -------------------------------------
# Page 1 tests.


def test_prj2_page1_img_elements(sample_prj2):
    """Test <img>'s of prj2's page_1, and their attributes."""
    content = Path(sample_prj2.outdir, "page_1.html").read_text()
    html = etree.HTML(content)
    imgs = html.xpath("//img")
    number_of_images_expected_in_page_1 = 3

    assert len(imgs) == number_of_images_expected_in_page_1

    elem_attrs = [
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.png",
            "style": "width: 200px;",
        },
        {
            "alt": "The symbol of peace",
            "src": "_images/peace.png",
            "style": "width: 200px;",
        },
        {
            "alt": "A tree icon",
            "src": "_images/tree.png",
            "style": "width: 200px;",
        },
    ]

    for index, img in enumerate(imgs):
        for k, v in elem_attrs[index].items():
            assert img.get(k) == v


def test_prj2_page1_figure_elements(sample_prj2):
    """Test <figure>'s of prj2's page_1, and their attributes."""
    content = Path(sample_prj2.outdir, "page_1.html").read_text()
    html = etree.HTML(content)
    figures = html.xpath("//figure")
    number_of_figures_expected_in_page_1 = 2

    assert len(figures) == number_of_figures_expected_in_page_1

    elem_attrs = [
        {
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "The symbol of peace",
                "src": "_images/peace.png",
                "style": "width: 200px;",
            },
        },
        {
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A tree icon",
                "src": "_images/tree.png",
                "style": "width: 200px;",
            },
        },
    ]

    for index, figure in enumerate(figures):
        assert elem_attrs[index]["css_cls"] == figure.get("class")
        img = figure.find("a").find("img")
        img_attrs = elem_attrs[index]["img_attrs"]
        for k, v in img_attrs.items():
            assert img.get(k) == v


# -------------------------------------
# Page 2 tests.


def test_prj2_page2_img_elements(sample_prj2):
    """Test <img>'s of prj2's page_2, and their attributes."""
    content = Path(sample_prj2.outdir, "page_2.html").read_text()
    html = etree.HTML(content)
    imgs = html.xpath("//img")
    number_of_images_expected_in_page_2 = 3

    assert len(imgs) == number_of_images_expected_in_page_2

    elem_attrs = [
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/balloon.light.png",
            "data-alt-src-color-scheme-dark": "_images/balloon.dark.png",
        },
        {
            "alt": "The symbol of peace",
            "src": "_images/peace.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/peace.light.png",
            "data-alt-src-color-scheme-dark": "_images/peace.dark.png",
        },
        {
            "alt": "A tree icon",
            "src": "_images/tree.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/tree.light.png",
            "data-alt-src-color-scheme-dark": "_images/tree.dark.png",
        },
    ]

    for index, img in enumerate(imgs):
        for k, v in elem_attrs[index].items():
            assert img.get(k) == v


def test_prj2_page2_figure_elements(sample_prj2):
    """Test <figure>'s of prj2's page_2, and their attributes."""
    content = Path(sample_prj2.outdir, "page_2.html").read_text()
    html = etree.HTML(content)
    figures = html.xpath("//figure")
    number_of_figures_expected_in_page_2 = 2

    assert len(figures) == number_of_figures_expected_in_page_2

    elem_attrs = [
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "The symbol of peace",
                "src": "_images/peace.light.png",
                "width": "200",
                "data-alt-src-color-scheme-light": "_images/peace.light.png",
                "data-alt-src-color-scheme-dark": "_images/peace.dark.png",
            },
        },
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A tree icon",
                "src": "_images/tree.light.png",
                "width": "200",
                "data-alt-src-color-scheme-light": "_images/tree.light.png",
                "data-alt-src-color-scheme-dark": "_images/tree.dark.png",
            },
        },
    ]

    for index, figure in enumerate(figures):
        assert elem_attrs[index]["css_cls"] == figure.get("class")
        img = figure.find("a").find("img")
        img_attrs = elem_attrs[index]["img_attrs"]
        for k, v in img_attrs.items():
            assert img.get(k) == v


# -------------------------------------
# Page 3 tests.


def test_prj2_page3_img_elements(sample_prj2):
    """Test <img>'s of prj2's page_3, and their attributes."""
    content = Path(sample_prj2.outdir, "page_3.html").read_text()
    html = etree.HTML(content)
    imgs = html.xpath("//img")
    number_of_images_expected_in_page_3 = 6

    assert len(imgs) == number_of_images_expected_in_page_3

    elem_attrs = [
        {  # image directive.
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.png",
            "style": "width: 200px;",
        },
        {  # cs_image directive.
            "alt": "A balloon icon",
            "class": "align-left",
            "src": "_images/balloon.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/balloon.light.png",
            "data-alt-src-color-scheme-dark": "_images/balloon.dark.png",
        },
        {  # figure directive.
            "alt": "The symbol of peace",
            "src": "_images/peace.png",
            "style": "width: 200px;",
        },
        {  # cs_figure directive.
            "alt": "The symbol of peace",
            "src": "_images/peace.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/peace.light.png",
            "data-alt-src-color-scheme-dark": "_images/peace.dark.png",
        },
        {  # figure directive.
            "alt": "A tree icon",
            "src": "_images/tree.png",
            "style": "width: 200px;",
        },
        {  # cs_figure directive.
            "alt": "A tree icon",
            "src": "_images/tree.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/tree.light.png",
            "data-alt-src-color-scheme-dark": "_images/tree.dark.png",
        },
    ]

    for index, elem in enumerate(imgs):
        for k, v in elem_attrs[index].items():
            assert elem.get(k) == v


def test_prj2_page3_figure_elements(sample_prj2):
    """Test <figure>'s of prj2's page_3, and their attributes."""
    content = Path(sample_prj2.outdir, "page_3.html").read_text()
    html = etree.HTML(content)
    figures = html.xpath("//figure")
    number_of_figures_expected_in_page_3 = 4

    assert len(figures) == number_of_figures_expected_in_page_3

    elem_attrs = [
        {
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "The symbol of peace",
                "src": "_images/peace.png",
                "style": "width: 200px;",
            },
        },
        {
            "css_cls": "align-left",
            "img_attrs": {
                "alt": "The symbol of peace",
                "src": "_images/peace.light.png",
                "width": "200",
                "data-alt-src-color-scheme-light": "_images/peace.light.png",
                "data-alt-src-color-scheme-dark": "_images/peace.dark.png",
            },
        },
        {
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A tree icon",
                "src": "_images/tree.png",
                "style": "width: 200px;",
            },
        },
        {
            "css_cls": "align-left",
            "img_attrs": {
                "alt": "A tree icon",
                "src": "_images/tree.light.png",
                "width": "200",
                "data-alt-src-color-scheme-light": "_images/tree.light.png",
                "data-alt-src-color-scheme-dark": "_images/tree.dark.png",
            },
        },
    ]

    for index, figure in enumerate(figures):
        assert elem_attrs[index]["css_cls"] == figure.get("class")
        img = figure.find("a").find("img")
        img_attrs = elem_attrs[index]["img_attrs"]
        for k, v in img_attrs.items():
            assert img.get(k) == v


# ---------------------------------------------------------------------
# Sample Project 3 tests.


def test_prj3_builds_successfully(sample_prj3):
    """Test that the project has built without problems."""
    index = Path(sample_prj3.outdir, "index.html").read_text()
    assert "Sample Project 3" in index


def test_prj3_page1_img_elements(sample_prj3):
    """Test <img>'s of prj3's page_1, and their attributes."""
    content = Path(sample_prj3.outdir, "page_1.html").read_text()
    html = etree.HTML(content)
    imgs = html.xpath("//img")
    number_of_img_expected_in_page_1 = 2

    assert len(imgs) == number_of_img_expected_in_page_1

    # Both images are identical. The only difference is the use of the
    elem_attrs = [
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.en.png",
            "style": "width: 200px;",
        },
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.en.png",
            "style": "width: 200px;",
        },
    ]

    for index, img in enumerate(imgs):
        for k, v in elem_attrs[index].items():
            assert img.get(k) == v


def test_prj3_page2_img_elements(sample_prj3):
    """Test <img>'s of prj3's page_2, and their attributes."""
    content = Path(sample_prj3.outdir, "page_2.html").read_text()
    html = etree.HTML(content)
    imgs = html.xpath("//img")
    number_of_img_expected_in_page_2 = 2

    assert len(imgs) == number_of_img_expected_in_page_2

    # Both images are identical. The only difference is the use of the
    elem_attrs = [
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.en.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/balloon.en.light.png",
            "data-alt-src-color-scheme-dark": "_images/balloon.en.dark.png",
        },
        {
            "alt": "A balloon icon",
            "class": "align-right",
            "src": "_images/balloon.en.light.png",
            "width": "200",
            "data-alt-src-color-scheme-light": "_images/balloon.en.light.png",
            "data-alt-src-color-scheme-dark": "_images/balloon.en.dark.png",
        },
    ]

    for index, img in enumerate(imgs):
        for k, v in elem_attrs[index].items():
            assert img.get(k) == v


def test_prj3_page3_figure_elements(sample_prj3):
    """Test <figure>'s of prj3's page_3, and their attributes."""
    content = Path(sample_prj3.outdir, "page_3.html").read_text()
    html = etree.HTML(content)
    figures = html.xpath("//figure")
    number_of_figures_expected_in_page_3 = 2

    assert len(figures) == number_of_figures_expected_in_page_3

    elem_attrs = [
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A balloon icon",
                "src": "_images/balloon.en.png",
                "style": "width: 200px;",
            },
        },
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A balloon icon",
                "src": "_images/balloon.en.png",
                "style": "width: 200px;",
            },
        },
    ]

    for index, figure in enumerate(figures):
        assert elem_attrs[index]["css_cls"] == figure.get("class")
        img = figure.find("a").find("img")
        img_attrs = elem_attrs[index]["img_attrs"]
        for k, v in img_attrs.items():
            assert img.get(k) == v


def test_prj3_page4_figure_elements(sample_prj3):
    """Test <figure>'s of prj3's page_3, and their attributes."""
    content = Path(sample_prj3.outdir, "page_4.html").read_text()
    html = etree.HTML(content)
    figures = html.xpath("//figure")
    number_of_figures_expected_in_page_4 = 2

    assert len(figures) == number_of_figures_expected_in_page_4

    light_path = "_images/balloon.en.light.png"
    dark_path = "_images/balloon.en.dark.png"

    elem_attrs = [
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A balloon icon",
                "src": light_path,
                "width": "200",
                "data-alt-src-color-scheme-light": light_path,
                "data-alt-src-color-scheme-dark": dark_path,
            },
        },
        {  # alt, img_attributes
            "css_cls": "align-right",
            "img_attrs": {
                "alt": "A balloon icon",
                "src": light_path,
                "width": "200",
                "data-alt-src-color-scheme-light": light_path,
                "data-alt-src-color-scheme-dark": dark_path,
            },
        },
    ]

    for index, figure in enumerate(figures):
        assert elem_attrs[index]["css_cls"] == figure.get("class")
        img = figure.find("a").find("img")
        img_attrs = elem_attrs[index]["img_attrs"]
        for k, v in img_attrs.items():
            assert img.get(k) == v
