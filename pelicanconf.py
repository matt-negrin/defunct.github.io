#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Negrin'
SITENAME = u'Matt Negrin'
SITEURL = 'https://matt-negrin.github.io'
SITENAME = "Matt Negrin's Blog"
SITESUBTITLE = 'Data Scientist - Birchbox'
SITELOGO = '/images/bitm.png'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

THEME = 'themes/Flex'
PYGMENTS_STYLE = 'native'
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

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mattnegrin'),
          ('github', 'https://github.com/matt-negrin'),
          ('envelope-o', 'https://mail.google.com/mail/?view=cm&fs=1&to=matt.negrin@gmail.com'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

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
PLUGIN_PATHS=['pelican-plugins','plugins']
PLUGINS=['liquid_tags.notebook','liquid_tags.include_code','ipynb.liquid', 'pelican_youtube',]
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'}}

MARKDOWN = {
  'extension_configs': {
    'pyembed.markdown': {}
  }
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
