#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Negrin'
SITENAME = u'Matt Negrin'
SITEURL = 'https://matt-negrin.github.io'
SITENAME = "Lazy Learning"
SITESUBTITLE = '''Taco and data enthusiast.
Currently a data scientist at Birchbox.
A blog mostly about statistics and machine learning, but I'm probably still thinking about tacos.'''
#Flex: SITELOGO = '/images/bitm.png'
SITEIMAGE = '/images/bitm.png'
DESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
# FAVICON = '/images/favicon.ico'
RFG_FAVICONS = '/images/favicon.ico'
# BROWSER_COLOR = '#333333'
HIDE_AUTHORS = True

DIRECT_TEMPLATES = ['index', 'tags', 'archives']
SITEMAP_SAVE_AS = 'sitemap.xml'

#Flex: THEME = 'themes/Flex'
THEME = 'themes/pelican-alchemy/alchemy'
PYGMENTS_STYLE = 'monokai'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

ROBOTS = 'index, follow'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

# LINKS = (('Pelican', 'http://getpelican.com/'),)

ICONS = (('linkedin', 'https://www.linkedin.com/in/mattnegrin'),
          ('github', 'https://github.com/matt-negrin'),
          ('envelope-o', 'https://mail.google.com/mail/?view=cm&fs=1&to=matt.negrin@gmail.com'),)

# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

STATIC_PATHS = ['images', 'notebooks', 'extras', 'code']

USE_LESS = False

NOTEBOOK_DIR = ['notebooks']
# CODE_DIR = ['code']

#Article and page pretty urls
# ARTICLE_URL = '{slug}/'
# ARTICLE_SAVE_AS = '{slug}/index.html'
# PAGE_URL = '{slug}/'
# PAGE_SAVE_AS = '{slug}/index.html'

MARKUP=('md','ipynb')
PLUGIN_PATHS=['plugins/pelican-plugins','plugins']
PLUGINS=['pelican-bootstrapify','pelican-ipynb.liquid', 'liquid_tags.notebook','liquid_tags.include_code',]
# 'pelican_youtube',
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'}}

MARKDOWN = {
  'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.meta', 'markdown.extensions.fenced_code'],
  'extension_configs': {
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'pyembed.markdown': {}
    # 'codehilite(linenums = True)' : {}
  }
}

# MARKDOWN =['fenced_code', 'codehilite(css_class=highlight)', 'extra',]
# MARKDOWN = {'extension_configs': {'pyembed.markdown': {}}}]



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
