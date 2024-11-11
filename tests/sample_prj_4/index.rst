.. Sample Project 4 documentation master file, created by
   sphinx-quickstart on Thu Oct 31 10:35:14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sample Project 4
================

This example Sphinx project should display warning messages at build time.
The reason is that the URIs used in both, ``cs_image`` and ``cs_figure``, do not exist in the filesystem.

The goal of this sample project is to verify whether the function ``get_image_paths``, in the ``sphinx_colorschemed_images.extension`` module, calls ``logger.warning`` when a candidate image does not exist. The test also checks whether ``logger.warning``, from ``sphinx.environment.collectors.asset``,  is also called.

The test case is ``tests/test_extension.py::test_prj4_has_wrong_image_uri``.

Below it includes the following directives:

.. code-block:: reStructuredText

   .. cs_image:: img/image_none.png
      :alt: A balloon icon
      :align: right
      :width: 200

   .. cs_figure:: img/figure_node.png
      :alt: A balloon icon
      :align: right
      :width: 200

      Nothing here

.. cs_image:: img/image_none.png
   :alt: A balloon icon
   :align: right
   :width: 200

.. cs_figure:: img/figure_none.png
   :alt: A balloon icon
   :align: right
   :width: 200

   Nothing here