"""A Sphinx extension to add support for colorschemed images."""

from .extension import copy_colorschemed_images, extension_builder_inited

__version__ = "0.1.0"


def setup(app) -> dict:
    app.add_config_value("csi_color_schemes", ["light", "dark"], "html")
    app.add_config_value("csi_default_color_scheme", "light", "html")
    app.add_config_value(
        "csi_image_path_pattern", "{path}/{basename}.{colorscheme}{ext}", "html"
    )
    # app.add_config_value("csi_include_js_script", True, "html")

    app.connect("builder-inited", extension_builder_inited)
    app.connect("build-finished", copy_colorschemed_images)

    app.add_js_file("sphinx-colorschemed-images.js")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
