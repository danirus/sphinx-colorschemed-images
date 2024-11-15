.. _users-guide:

User's Guide
############

Installation
************

To use sphinx-colorschemed-images, pip install the package with:

.. code-block::

    pip install sphinx-colorschemed-images

Then modify your ``conf.py`` file and add it to your ``extensions`` setting:

.. code-block::

    extensions = [
        'sphinx_colorschemed_images',
    ]

Now your project is ready to use the ``cs_image`` and the ``cs_figure`` directives.


Motivation
**********

The usual way to add an image to a Sphinx project is by using the ``image`` directive:

.. grid:: 2
   :class-container: py-2
   :gutter: 3

   .. grid-item-card::

      In Markdown with ``myst-parser``:

      .. code-block:: markdown

         ```{image} img/balloon.light.png
         :alt: A balloon icon
         :width: 200
         :align: center
         ```

   .. grid-item-card::

      Or in reStructuredText:

      .. code-block:: reStructuredText

         .. image:: img/balloon.light.png
            :alt: A balloon icon
            :align: center
            :width: 200

.. image:: img/balloon.light.png
   :alt: A balloon icon
   :align: center
   :width: 200

----

Modern operating systems and web browsers support by default two color schemes, light and dark. But the ``image`` and ``figure`` directives produce an ``<img>`` tag with a single URI, as in the example above.

To include the **dark** version of the previous balloon a second ``image`` directive is required:

.. grid:: 2
   :class-container: py-2
   :gutter: 3

   .. grid-item-card::

      In Markdown with ``myst-parser``:

      .. code-block:: markdown

         ```{image} img/balloon.dark.png
         :alt: A balloon icon
         :width: 200
         :align: center
         ```

   .. grid-item-card::

      Or in reStructuredText:

      .. code-block:: reStructuredText

         .. image:: img/balloon.dark.png
            :alt: A balloon icon
            :align: center
            :width: 200

Which produces the following ``<img>`` tag:

.. code-block:: html

   <img alt="A balloon icon" class="align-center"
      src="_images/balloon.dark.png"
      width="200">

.. image:: img/balloon.dark.png
   :alt: A balloon icon
   :align: center
   :width: 200

The ``cs_image`` directive
**************************

The ``cs_image`` directive extends the functionality of the ``image`` directive by looking for two image files for the given URI, one for each color scheme. The directive generates an ``<img>`` tag with ``data`` attributes that facilitate the switch between **light** and **dark** color schemes.

The following ``cs_image`` directive:

.. grid:: 2
   :class-container: py-2
   :gutter: 3

   .. grid-item-card::

      In Markdown with ``myst-parser``:

      .. code-block:: markdown

         ```{cs_image} img/balloon.png
         :alt: A balloon icon
         :width: 200
         :align: center
         ```

   .. grid-item-card::

      Or in reStructuredText:

      .. code-block:: reStructuredText

         .. cs_image:: img/balloon.png
            :alt: A balloon icon
            :align: center
            :width: 200

Produces the following ``<img>`` tag:

.. code-block:: html

   <img alt="A balloon icon" class="align-center"
      data-alt-src-color-scheme-dark="_images/balloon.dark.png"
      data-alt-src-color-scheme-light="_images/balloon.light.png"
      src="_images/balloon.dark.png"
      width="200">

.. cs_image:: img/balloon.png
   :alt: A balloon icon
   :align: center
   :width: 200

Switch the color scheme by using the selector at the top right of the header, or change it in your operating system settings. The balloon image will switch automatically between **light** and **dark** color-schemes.

The ``cs_figure`` directive
***************************

The ``cs_figure`` directive extends the functionality of the ``figure`` directive by looking for two image files for the given URI, one for each color scheme. The directive generates an ``<img>`` tag with ``data`` attributes that facilitate the switch between **light** and **dark** color schemes.

The following ``cs_figure`` directive:

.. grid:: 2
   :class-container: py-2
   :gutter: 3

   .. grid-item-card::

      In Markdown with ``myst-parser``:

      .. code-block:: markdown

         ```{cs_figure} img/peace.png
         :alt: An icon for peace
         :width: 200
         :align: right

         The caption of the figure.
         ```

   .. grid-item-card::

      Or in reStructuredText:

      .. code-block:: reStructuredText

         .. cs_figure:: img/peace.png
            :alt: An icon for peace
            :align: right
            :width: 200

            The caption of the figure.

Produces the following ``<img>`` tag:

.. code-block:: html

    <figure class="align-right" id="id3">
      <a class="reference internal image-reference"
         href="_images/peace.light.png">
        <img alt="An icon for peace"
          data-alt-src-color-scheme-dark="_images/peace.dark.png"
          data-alt-src-color-scheme-light="_images/peace.light.png"
          src="_images/peace.dark.png" width="200">
      </a>
      <figcaption>
        <p>
          <span class="caption-text">The caption of the figure.</span>
          <a class="headerlink" href="#id3" title="Link to this image">¶</a>
        </p>
      </figcaption>
    </figure>

.. cs_figure:: img/peace.png
    :alt: An icon for peace
    :align: right
    :width: 200

    The caption of the figure.

Switch the color scheme by using the selector at the top right of the header, or change it in your operating system settings. The balloon image will switch automatically between **light** and **dark** color-schemes.


Extension's settings
********************

The functionality of the extension can be customized via 4 settings:

* ``csi_color_schemes``
* ``csi_default_color_scheme``
* ``csi_image_path_pattern``
* ``csi_add_script_to_html_output``


Setting ``csi_color_schemes``
=============================

It defaults to ``["light", "dark"]``.

It can be overriden, but so far web browsers can only be queried about whether the preferred color scheme is ``light`` or ``dark``.

If you override this setting (or if your theme does), include an HTML meta tag with the color schemes:

.. code-block:: HTML

    <meta name="color-scheme" content="lightblue darkblue lightred darkred" />

The JavaScript plugin included with the extension reads the meta tag to know about the available color-schemes, when they are other than the default ``light`` and ``dark``.


Setting ``csi_default_color_scheme``
====================================

It defaults to ``"light"``.

By default the URI used for the ``src`` attribute in ``cs_image`` and ``cs_figure`` directives correspond to the ``light`` version of the URI. The effect of overriding it to ``"dark"`` is that the ``src`` attribute of the ``<img>`` tag will refer to the dark color-schemed image.

This is only noticeable when the theme of your Sphinx project is not color-scheme aware (i.e: the **Alabaster** theme).


Setting ``csi_image_path_pattern``
==================================

It defaults to ``"{path}/{basename}.{colorscheme}{ext}"``.

This setting represents the pattern that matches the URI (given in the directives ``cs_image`` and ``cs_figure``) with files in the image directory.

It is required that the name of the color scheme, represented by the placeholder ``{colorscheme}``, is part of the filename of the image, and not part of a directory.

.. warning::

    The ``{colorscheme}`` placeholder can not be part of a directory name, as Sphinx copies image files to a directory named ``_images`` in the build directory, but it does not create the original directory structure.

    The following two ``image`` directives will display the same file:

    .. code-block:: reStructuredText

        .. image:: img/dir1/balloon.png
            :alt: A balloon icon
            :align: center
            :width: 200

        .. image:: img/dir2/balloon.png
            :alt: A balloon icon
            :align: center
            :width: 200

    Sphinx uses ``dir1`` and ``dir2`` to find the sources of the two files, and copies them, named identically to the destination directory ``_images/balloon.png``. So only one of the two files survives. Only one is made available in the built ``_images/`` directory.


Internationalized Sphinx projects usually maintain different images or figures for different languages by using the ``figure_language_filename`` [1]_. In such projects you can use ``csi_image_path_pattern`` in the same way, including the ``{language}`` placeholder as part of the filename:

.. code-block:: python

   csi_image_path_pattern = "{path}/{basename}.{language}.{colorscheme}{ext}"

Setting ``csi_add_script_to_html_output``
=========================================

It defaults to ``True``.

When ``True``, Sphinx will add the following HTML ``<script>`` tag to the output:

.. code-block:: HTML

    <script src="_static/sphinx-colorschemed-images.js?v=abcdefg"></script>

The ``sphinx-colorschemed-images.js`` is in charge of changing between color-schemed version of images.

The npm package `sphinx-colorschemed-images <https://www.npmjs.com/package/sphinx-colorschemed-images>`_ provides a class ``SphinxColorschemeImageHandler`` that offers the posibility to disable the automatic switching of images, leaving such control to the developer. That way, if your Sphinx theme implements color-schemes other than ``light`` and ``dark``, you could control the transition directly with the method ``activate`` of such class.

Read the :ref:`javascript` page to see an example.

----

.. [1] ``figure_language_filename`` is the `filename format for language-specific figures <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-figure_language_filename>`_.
