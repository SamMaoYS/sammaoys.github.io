AUTHOR = 'Yongsen Mao'
SITENAME = 'Yongsen Mao'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']

TIMEZONE = 'Canada/Pacific'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'https://github.com/SamMaoYS'),)

# Social widget
SOCIAL = (('Email', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']
# PAGINATED_TEMPLATES = {'archives': None, 'tag': None, 'category': None, 'author': None}

FORMATTED_FIELDS = ['summary']
FORMATTED_FIELDS += ['landing']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/plugins', 'pelican-plugins']
PLUGINS = ['m.abbr',
           'm.code',
           'm.components',
           'm.dox',
           'm.filesize',
           'm.gl',
           'm.gh',
           'm.htmlsanity',
           'm.images']

M_FAVICON = ('favicon.ico', 'image/x-ico')
M_BLOG_FAVICON = ('favicon-blog.png', 'image/png')

M_SITE_LOGO_TEXT = 'Yongsen Mao'

M_LINKS_NAVBAR1 = [('Home', '/', 'home', []),
                   ('CV', '/', 'cv', []),
                   ('Blog', '/', 'blog', [])]

# M_LINKS_FOOTER3 = [('Contact', ''),
#                    ('E-mail', 'mailto:you@your.brand'),
#                    ('GitHub', 'https://github.com/your-brand')]

M_FINE_PRINT = """Powered by `Pelican <https://getpelican.com>`_ and `m.css <https://mcss.mosra.cz>`_."""