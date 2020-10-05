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
SOCIAL = (('github-circle', 'http://github.com/yeolab'),
          ('twitter-circle', 'http://twitter.com/yeo_lab')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "twenty-pelican-html5up"

# TAGLINE = "#YEOLO"
DISQUS_SITENAME = "yeolab"

TYPOGRIFY = True
GOOGLE_ANALYTICS = "UA-75886209-1"

MENUITEMS = [('Research', '/research/'),
             ('Papers', '/papers/'),
            #  ('People', '/people/'),
            #  ('Photos', '/gallery/'),
             ('Funding', '/funding/'),
            #  ('Collaborators', '/collaborators/'),
             ('Software', '/software/'),
             ('Links', '/links/'),
	     ('Books', '/books/'
]

# IPython notebook blog posts
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['.', 'pelican-plugins']
PLUGINS = [
    # Make "team" page of people in lab, with different positions
    'people',

    # Make gallery pages
    # 'gdrivegallery'
    ]
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

# Resize gallery images to 200x200
IMAGE_PATH = 'gallery'
RESIZE = [
        ('gallery', False, 200,200),
      ]

# Order of the positions of people to put in the website, ie.g. PI first,
# Then senior scientsits, postdocs, grad students, etc
# The list is pairs of (display_name, matching_name), where "display name"
# is what is actually shown, and "matching_name" is what matches in the
# "position" metadata of the person's page
PEOPLE_POSITION_ORDER = [
    # (Possibly plural name), (Singular name)
    ('Principal Investigator', 'Principal Investigator'),
    ('Project Scientists', 'Project Scientist'),
    ('Post-Doctoral Fellows', 'Post-Doctoral Fellow'),
    ('PhD Students', 'Graduate Student'),
    ('Masters Students','Masters Student'),
    ('Visiting Scientists', 'Visiting Scientists'),
    ('Visiting Graduate Students', 'Visiting Graduate Student'),
    ('Staff', 'Staff'),
    ('Undergraduate Students', 'Undergraduate Student'),
    ('High School Students', 'High School Student'),
    ]


# Thumbnailer Configuration
IMAGE_PATH = 'images/gallery/'
THUMBNAIL_DIR = 'images/gallery/thumbnails'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True

DEFAULT_THUMBNAIL_SIZES = {
    'thumbnail_square': '100',
    'thumbnail_wide': '100x?',
    'thumbnail_tall': '?x100',
}
