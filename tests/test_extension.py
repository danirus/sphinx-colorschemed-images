from unittest import mock

import pytest
import sphinx
from sphinx.locale import __

from sphinx_colorschemed_images.exceptions import CSIExtensionError

SPHINX_VERSION = sphinx.__version__


def test_prj2_with_wrong_csi_image_path_pattern(test_app):
    """Test the sample_prj_2 using a wrong formed csi_image_path_pattern."""
    wrong_csi_image_path_pattern = "{paz}/{beisneim}.{coloresquim}{ext}"
    with pytest.raises(CSIExtensionError) as excinfo:
        test_app(
            buildername="html",
            srcdir="sample_prj_2",
            confoverrides={
                "csi_image_path_pattern": wrong_csi_image_path_pattern,
            },
        )

    assert excinfo.value.args[0] == (
        "Invalid csi_image_path_pattern: "
        f'"{wrong_csi_image_path_pattern}" - '
        "KeyError('paz')"
    )


@mock.patch("sphinx_colorschemed_images.extension.logger")
@mock.patch("sphinx.environment.collectors.asset.logger")
def test_prj4_has_wrong_image_uri(sphinx_logger, csi_logger, test_app):
    """Test sample_prj_4, whose image directive refers to non-existing file."""
    test_app(buildername="html", srcdir="sample_prj_4")

    assert sphinx_logger.warning.called
    assert sphinx_logger.warning.call_count == 2  # noqa: PLR2004

    if SPHINX_VERSION.startswith("7.3."):
        assert sphinx_logger.warning.call_args_list[0].args == (
            "image file not readable: img/image_none.png",
        )
        assert sphinx_logger.warning.call_args_list[1].args == (
            "image file not readable: img/figure_none.png",
        )
    else:
        assert sphinx_logger.warning.call_args_list[0].args == (
            __("image file not readable: %s"),
            "img/image_none.png",
        )
        assert sphinx_logger.warning.call_args_list[1].args == (
            __("image file not readable: %s"),
            "img/figure_none.png",
        )

    assert csi_logger.warning.called
    assert csi_logger.warning.call_count == 4  # noqa: PLR2004
    assert csi_logger.warning.call_args_list[0].args == (
        __("image not found: %s"),
        "img/image_none.en.light.png",
    )
    assert csi_logger.warning.call_args_list[1].args == (
        __("image not found: %s"),
        "img/image_none.en.dark.png",
    )
    assert csi_logger.warning.call_args_list[2].args == (
        __("image not found: %s"),
        "img/figure_none.en.light.png",
    )
    assert csi_logger.warning.call_args_list[3].args == (
        __("image not found: %s"),
        "img/figure_none.en.dark.png",
    )
