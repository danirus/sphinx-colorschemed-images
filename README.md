# Color schemed images for Sphinx  [![tests](https://github.com/danirus/sphinx-colorschemed-images/workflows/tests/badge.svg)](https://github.com/danirus/sphinx-colorschemed-images/actions/workflows/tests.yml)

An extension for [Sphinx](https://www.sphinx-doc.org/en/master/) that adds support for color-scheme aware images. This `README.md` is also used for the NodeJS package. The NodeJS package contains only the JavaScript module. See below the paragraph about the JavaScript plugin.

## Tested

* [Tested against Sphinx 7.3, 7.4, 8.0 and 8.1](https://github.com/danirus/sphinx-colorschemed-images/actions/workflows/tests.yml), see matrix python-tests.
* [Tested with NodeJS v20](https://github.com/danirus/sphinx-colorschemed-images/actions/workflows/tests.yml), see javascript-tests.

## Description

Sphinx Color Schemed Images is an extension that makes available two new image directives to your project:

* `cs_image` extends the `image` directive, and
* `cs_figure` extends the `figure` directive.

These new directives add data attributes to the HTML `<img>` tag to help web browsers to automatically transition between **light** and **dark** color schemes. The extension adds a bit of JavaScript code to trigger an image update when the user switches the color scheme.

## Usage

Install the package:

    pip install sphinx-colorschemed-images

Add `sphinx_colorschemed_images` to the `extensions` setting, in your project's `conf.py` file.

As an example, download the following files and place them in the source directory of your Sphinx project, inside the image directory. I assume the sources are in the `docs/` directory, and the image directory is `docs/img/`:

* [img/balloon.light.png](https://raw.githubusercontent.com/danirus/sphinx-colorschemed-images/refs/heads/main/tests/sample_prj_2/img/balloon.light.png)
* [img/balloon.dark.png](https://raw.githubusercontent.com/danirus/sphinx-colorschemed-images/refs/heads/main/tests/sample_prj_2/img/balloon.dark.png)

Now edit your `index.rst` or `index.md` file, and add a `cs_image` directive. For `index.rst`, add:

    .. cs_image:: img/balloon.png
       :alt: A balloon icon
       :align: center
       :width: 200

If it is an `index.md`, add the following instead:

    ```{cs_image} img/balloon.png
    :alt: A balloon icon
    :align: center
    :width: 200
    ```

Build your Sphinx project and serve it. You should see either the image for the light color scheme, `balloon.light.png`, or the image for the dark color scheme, `balloon.dark.png`. Switch your operating system settings and the image should update automatically.

## JavaScript plugin

When using the extension Sphinx adds a script to your HTML output, `sphinx-colorschemed-images.js`, that listens for changes on the user's preferred color-scheme and switches between the images accordingly. It works in all Sphinx themes regardless of whether they have support for light/dark color schemes.

If you have your own theme and it offers the user control over the color-scheme, you can use the NPM package [sphinx-colorschemed-images](https://www.npmjs.com/package/sphinx-colorschemed-images) and its class `SphinxColorschemeImageHandler` when building your own plugin.

The source code is rather small, so it is better to look into [it](https://raw.githubusercontent.com/danirus/sphinx-colorschemed-images/refs/heads/main/js/src/main.js) than to explain it here. If your theme already listens for changes in `prefers-color-scheme`, pass `{auto: false}` to the constructor, to avoid adding the listeners again. To switch between *light* and *dark* images, call the `activate` method with either `light` or `dark`.

## Contributing

The Makefile is the lead for all development tasks. Mind the tests in Python and JavaScript.

Appropriate documentation will come soon.
