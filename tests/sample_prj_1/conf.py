# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sample Project 1'
copyright = '2024, copyright'
author = 'Daniela Rus Morales'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_colorschemed_images',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_nefertiti'
html_static_path = ['_static']

# - Settings for the Sphinx Colorschemed Images extension --------------------

# csi_color_schemes defaults to:
csi_color_schemes = ["light", "dark"]

# Building the project should fail, as the csi_color_schemes list does
# not include the value of the csi_default_color_scheme setting.
csi_default_color_scheme = "unknown"
