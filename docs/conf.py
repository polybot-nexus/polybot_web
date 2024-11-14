# Project Information
project = 'Polybot Nexus'
copyright = '2024, Aikaterini Vriza'
author = 'Aikaterini Vriza'
release = '1.0'

# Sphinx Extensions
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_design'
]

# nbsphinx Settings
nbsphinx_codecell_lexer = 'none'

# Templates Path
templates_path = ['_templates']

# Exclude Patterns
exclude_patterns = []

# HTML Output Options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Add the Logo
html_logo = '_static/polybot_logo.png'  # Replace with the path to your logo image

# Error Handling
nbsphinx_allow_errors = True
suppress_warnings = ['misc.highlighting_failure']
