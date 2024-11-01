# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Robotics Docs'
copyright = '2024, Jiahang Zhang'
author = 'Jiahang Zhang'

release = '0.1'
version = '0.0.1'
import sphinx_rtd_theme
# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# -- Options for EPUB output
epub_show_urls = 'footnote'
