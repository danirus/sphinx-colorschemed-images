.. Sample Project 3 documentation master file, created by
   sphinx-quickstart on Thu Oct 31 10:35:14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sample Project 3
================

This Sphinx project is a sample of a multi-language project.
Images contain the language code in their name, but URIs provided in the
directives vary: some include the language code, some don't. Each image or figure is provided in their own page (so that tests are simple).

This project uses the setting ``csi_image_path_pattern`` in the ``conf.py`` as:

.. code-block:: python

   csi_image_path_pattern = "{path}/{basename}.{language}.{colorscheme}{ext}"

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   page_1
   page_2
   page_3
   page_4