AUTHOR = 'Princiya Sequeira'
SITENAME = "P's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Blogroll
LINKS = (('About', 'https://princiya.com/'),
         ('Speaking', 'https://princiya.com/pages/talks.html'),
         ('Writing', 'https://princiya.com/blog'),
        ('Testimonials', 'https://princiya.com/pages/testimonials.html'), )

# Social widget
SOCIAL = (
    ("github", "https://github.com/princiya"),
    ("twitter", "https://twitter.com/princi_ya"),
    ("linkedin", "https://www.linkedin.com/in/princiya/"),
    ("rss", "/newblog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/newblog/archives.html"),
    ("Categories", "/newblog/categories.html"),
    ("Tags", "/newblog/tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/flex"

STATIC_PATHS = ['images']