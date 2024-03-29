# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Gamify IT'
copyright = '2022, Universität Stuttgart'
author = 'Universität Stuttgart'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build',
        'venv',
        'internal',
        'README.md',
        'adr/README.md',
        'install-manuals/README.md',
        'adr/adr-template.md',
        'template-README.md',
        '**/template*.md',
        'Thumbs.db',
        '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Generate HTML anchors (test#h1-title) for titles up to h4
myst_heading_anchors = 4

myst_enable_extensions = [
        'colon_fence', # :::$TYPE\n$CONTENT\n::: == ```$TYPE\n$CONTENT\n```
        'html_admonition', # :::{attention, caution, danger, error, hint, important, note, tip, warning} $TITLE\n$CONTENT\n::: -> renders a message with the given title and content in the given style
        'linkify', # www.google.com -> <www.google.com>
        'tasklist', # [ ] -> unchecked checkbox, [x] -> checked checkbox
        ]
