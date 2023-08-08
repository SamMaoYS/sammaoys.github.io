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

M_BLOG_NAME = 'Yongsen Mao Blog'
M_BLOG_URL = 'summary/'

# Social widget
SOCIAL = (('Email', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['archives']
PAGINATED_TEMPLATES = {'archives': None, 'tag': None, 'category': None, 'author': None}
FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']
M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

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
M_HIDE_ARTICLE_SUMMARY = True

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

M_LINKS_NAVBAR1 = [('Home', '/', 'home', []),
                   ('CV', 'cv/', 'cv', []),
                   ('Blog', 'blog/', 'blog', [
                       ('NeRFs', 'blog/nerfs/', 'blog/nerfs'),
                       ('Real-Time Rendering', 'blog/real-time_rendering/', 'blog/real-time_rendering'),
                   ])]

M_FINE_PRINT = """Powered by `Pelican <https://getpelican.com>`_ and `m.css <https://mcss.mosra.cz>`_."""
