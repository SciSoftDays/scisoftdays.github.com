#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os


AUTHOR = u'SciSoftDays Organizing Committee'
SITENAME = u'Scientific Software Days'
SITEURL = ''

TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Set the pages URL
#PAGE_URL = ('{category}/{slug}.html')

# Title menu options
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Home', '/'),
             ('Workshops', '/workshops.html'),
             ('News', '/archives.html')]
             
NEWEST_FIRST_ARCHIVES = False

# # Theme
THEME_DIR = os.path.join(os.getcwd(), "theme")
THEME_NAME = "tuxlite_tbs"
THEME = os.path.join(THEME_DIR, THEME_NAME)
RECENT_ARTICLES_COUNT = 3

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/scisoftdays'),
          ('Google+', 'https://plus.google.com/114759765621122794742'),
          )
#          ('Another social link', '#'),)
TWITTER_USERNAME = "scisoftdays"

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdf', 'CNAME']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
