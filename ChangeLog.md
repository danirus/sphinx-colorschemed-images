# Change Log

## [0.1.4] - 2024-11-21

- Image wrapping anchor requires to get its `href` attribute updated when switching color schemes. Add test case. Update docs.

## [0.1.3] - 2024-11-21

- Fix: Image node URI must be relative to path given in the document instead of path calculated by ``get_image_paths``.

## [0.1.2] - 2024-11-15

- Fix: Add sphinx_colorschemed_images/static directory to Python distribution.

## [0.1.1] - 2024-11-15

- Enhancement: When switching images for directive `cs_figure`, change as well the `href` attribute of the anchor used inside the `<figure>` element that wraps the image.
- Extend JavaScript tests to cover previous point.
- Add GitHub Actions workflows to publish the package in PyPY and the NPM registry.

## [0.1.0] - 2024-11-12

- Sphinx extension to add support for colorschemed images.
- Create Node.js package and Python package.
- Add JavaScript tests (Karma/Jasmine) and Python tests (PyTest/Tox, for multiple versions of Sphinx).
