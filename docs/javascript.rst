.. _javascript:

JavaScript
##########

When using the extension Sphinx adds the script ``sphinx-colorschemed-images.js`` to the HTML output.

Once the script is loaded in the browser, images added with the ``cs_image`` and ``cs_figure`` directives will be ready to switch color-schemes based on the ``prefers-color-scheme`` CSS media feature. Even when using Sphinx themes that does not read such a feature. In those cases, if the user changes the operating system setting from light to dark and viceversa the javascript module will switch the images accordingly.

Using the NPM package
*********************

If you are a theme developer and wanted to have more control over the automatic switching, you might want to use the JavaScript class ``SphinxColorschemeImageHandler`` provided with the NPM package `sphinx-colorschemed-images <https://www.npmjs.com/package/sphinx-colorschemed-images>`_.

To do so, npm install the package:

.. code-block:: bash

    npm i -D sphinx-colorschemed-images

And import the class in your JavaScript module:

.. code-block:: javascript

    import { SphinxColorschemeImageHandler } from "sphinx-colorschemed-images";

If your theme already reads the ``prefers-color-scheme`` CSS feature, pass ``{auto: false}`` to the class constructor:

.. code-block:: javascript

    const cSchemeImgHdl = SphinxColorschemeImageHandler({auto: false});

And call the method ``activate`` whenever you want the images to switch color-schemes:

.. code-block:: javascript

    if (mode !== 'auto')  {  // Assuming it is either 'light' or 'dark'.
        cSchemeImgHdl.activate(mode);
    }

This explanation is rather short. You might want to take a look at the `source code <https://github.com/danirus/sphinx-colorschemed-images/blob/main/js/src/main.js>`_ of the class for completeness, or to a use case in the module `cschemes.js <https://github.com/danirus/sphinx-nefertiti/blob/main/js/src/cschemes.js>`_ of the Nefertiti for Sphinx theme.
