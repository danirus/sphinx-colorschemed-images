# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_colorschemed_images

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-colorschemed-images'
copyright = '2024, Daniela Rus Morales'
author = 'Daniela Rus Morales'

release_pattern_url = (
    "https://sphinx-colorschemed-images.readthedocs.io/en/{release}/"
)

release = sphinx_colorschemed_images.__version__
releases = [release,]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_colorschemed_images',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

language = "en"

today_fmt = '%A %d. %B %Y, %H:%M'

html_theme = "sphinx_nefertiti"

html_theme = 'sphinx_nefertiti'
html_static_path = ['static']
html_favicon = "static/diamond-half.svg"

html_theme_options = {
    "documentation_font": "Open Sans",
    "documentation_font_size": "1.0rem",
    "monospace_font": "Ubuntu Mono",
    "monospace_font_size": "1.1rem",

    "style": "purple",
    "pygments_light_style": "pastie",
    "pygments_dark_style": "dracula",

    "logo": "diamond-half.svg",
    "logo_width": 24,
    "logo_height": 24,
    "logo_alt": "sphinx-colorschemed-images",

    "repository_url": "https://github.com/danirus/sphinx-colorschemed-images",
    "repository_name": "sphinx-colorschemed-images",

    "current_version": f"v{release}",
    "versions": [
        ("v%s" % item, release_pattern_url.format(release=item))
        for item in releases
    ],

    "footer_links": [
        {
            "text": "Documentation",
            "link": "https://sphinx-colorschemed-images.readthedocs.com",
        }, {
            "text": "Package",
            "link": "https://pypi.com/sphinx-colorschemed-images",
        }, {
            "text": "Repository",
            "link": "https://github.com/danirus/sphinx-colorschemed-images",
        }, {
            "text": "Issues",
            "link": "https://github.com/danirus/sphinx-colorschemed-images/issues",
        },
    ],
}

csi_add_script_to_html_output = False
