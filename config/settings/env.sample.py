from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'j-wc(!ttycc3-#yw+1dogy#ld*ro$s6bznm34_!b)os3ff3tf3'

#Application definition
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ['127.0.0.1']

ALLOWED_HOSTS = ['*']
