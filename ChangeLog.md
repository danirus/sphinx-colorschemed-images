# Release Notes

## [0.2.3] - 2025-06-17

- Skip copying light/dark images when the Sphinx builder will not use them, which is the case for builders: epub, gettext, latex, linkcheck, man, pseudoxml, texinfo, text, xml.

## [0.2.2] - 2024-11-26

- Fix: prevent calling method `report_messages` if `HTML5Translator` does not have it. It is here for compat reasons.

## [0.2.1] - 2024-11-26

- Fix: destination directory was not properly referred to when copying images.

## [0.2.0] - 2024-11-25

- Remove unnecessary `console.log`.

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
