#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'Olga Botvinnik'
SITENAME = u'Yeo Lab'
SITEURL = 'yeolab.github.io'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# DEFAULT_METADATA = {
#     'status': 'draft',
# }
# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Don't show article categories
DISPLAY_CATEGORIES_ON_MENU = False
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'

ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

# Save "about", "contact" as seprate html files
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# Don't show all pages in pages/ in the menu
DISPLAY_PAGES_ON_MENU = False


ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

# Blogroll
# LINKS =  (('Bioinformatics@UCSD', 'http://bioinformatics.ucsd.edu/'),
#           ('UCSD', 'http://ucsd.edu/'),
#           )
#
# # Social widget
# SOCIAL = (('github-square', 'http://github.com/gbic-ucsd'),
#           ('twitter-square', 'http://twitter.com/gbicucsd'),
#           ('facebook-square', 'http://facebook.com/gbicucsd'),
#           )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "twenty-pelican-html5up"

TAGLINE = "Dr. Gene Yeo's Laboratory at UC San Diego"
DISQUS_SITENAME = "yeolab"

TYPOGRIFY = True
# GOOGLE_ANALYTICS = "UA-53680167-1"


MENUITEMS = [('Research', '/research/'),
             ('Papers', '/papers/'),
             ('People', '/people/'),
             ('Software', '/software/'),
             ('Blog', '/blog/'),
]

# IPython notebook blog posts
MARKUP = ('md', 'ipynb')

PLUGINS = ['people']
# PLUGINS = ['ipynb']

IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')),
                            ('div', ('class', 'output'))]

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}


TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''


# Order of the positions of people to put in the website, ie.g. PI first,
# Then senior scientsits, postdocs, grad students, etc
# The list is pairs of (display_name, matching_name), where "display name"
# is what is actually shown, and "matching_name" is what matches in the
# "position" metadata of the person's page
PEOPLE_POSITION_ORDER = [('Principal Investigator', 'Principal Investigator'),
                         ('Project Scientists', 'Project Scientist'),
                         ('Post-Doctoral Fellows', 'Post-Doctoral Fellow'),
                         ('Graduate Students', 'Graduate Student'),
                         ('Staff', 'Staff')]
