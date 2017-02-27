#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Negrin'
SITENAME = u'Matt Negrin'
SITEURL = ''
SITENAME = "Matt Negrin's Blog"
SITESUBTITLE = 'Data Scientist at Birchbox'
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
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

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

STATIC_PATHS = ['images', 'notebooks']

USE_LESS = False

#Article and page pretty urls
# ARTICLE_URL = '{slug}/'
# ARTICLE_SAVE_AS = '{slug}/index.html'
# PAGE_URL = '{slug}/'
# PAGE_SAVE_AS = '{slug}/index.html'

MARKUP=('md','ipynb')
PLUGIN_PATHS=['pelican-plugins','plugins']
PLUGINS=['liquid_tags.notebook','ipynb.liquid',]
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

# EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'}, 'extras/.travis.yml': {'path': '.travis.yml'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
