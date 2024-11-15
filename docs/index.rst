.. sphinx-colorschemed-images documentation master file, created by
   sphinx-quickstart on Wed Oct 30 16:12:36 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sphinx-colorschemed-images
##########################

Sphinx Color Schemed Images is an extension that makes available two new image directives to your project:

* ``cs_image`` extends the ``image`` directive, and
* ``cs_figure`` extends the ``figure`` directive.

These new directives add data attributes to the HTML ``<img>`` tag to help web browsers to automatically transition between **light** and **dark** color schemes. The extension adds a bit of JavaScript code to trigger an image update when the user switches the color scheme.

Quick Start
***********

Install the package:

.. code-block::

    pip install sphinx-colorschemed-images

Modify your ``conf.py`` file and add it to your ``extensions`` setting:

.. code-block::

    extensions = [
        'sphinx_colorschemed_images',
    ]

Download the following files and place them in the source directory of your Sphinx project, inside the directory where you keep your images.

Let's assume your ``conf.py`` is in the ``docs/`` directory, along with your ``index.rst`` or ``index.md`` file, and there is a ``docs/img/`` directory where you will save the following files:

* `img/balloon.light.png <https://raw.githubusercontent.com/danirus/sphinx-colorschemed-images/refs/heads/main/tests/sample_prj_2/img/balloon.light.png>`_
* `img/balloon.dark.png <https://raw.githubusercontent.com/danirus/sphinx-colorschemed-images/refs/heads/main/tests/sample_prj_2/img/balloon.dark.png>`_

Now edit your ``index`` document and add the following ``cs_image`` directive:

.. tab-set::

    .. tab-item:: Markdown
        :sync: md

        .. code-block:: markdown

         ```{image} img/balloon.png
         :alt: A balloon icon
         :width: 200
         :align: center
         ```

    .. tab-item:: reStructuredText
        :sync: rst

        .. code-block:: reStructuredText

         .. image:: img/balloon.png
            :alt: A balloon icon
            :align: center
            :width: 200

The URI does not represent an actual filename in your directory. But it almost does. If you prefer it, use a wildcard character: ``img/balloon.*``.

Finally, build your Sphinx project and serve it. You should see either the image for the light color scheme or the image for the dark color scheme. Switch your operating system settings and the image should update automatically.

Keep reading the :ref:`users-guide` to find out more about the extension and to see some examples.

Index
*****

.. toctree::
   :maxdepth: 2

   users-guide
   javascript
