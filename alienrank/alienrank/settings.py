"""
Django settings for alienrank project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from __future__ import absolute_import

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.environ.get('PROJECT_HOME', os.path.join(os.path.dirname(os.path.dirname(__file__)), '../'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.alienrank.com',
    'arlocal.alienrank.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'djcelery',

    'rank',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'alienrank.urls'

WSGI_APPLICATION = 'alienrank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'alienrank'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "alienrank/templates"),
)

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "alienrank/static"),
)

STATIC_ROOT_URL = os.environ.get('STATIC_ROOT_URL', '')
ROOT_URL = os.environ.get('ROOT_URL', 'http://alienrank.com')


STATIC_URL = STATIC_ROOT_URL + '/static/'
MEDIA_URL = STATIC_ROOT_URL + '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'var/static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'var/media/')
LOG_ROOT = os.path.join(BASE_DIR, 'var/log/')

GA_TRACKING_ID = ''
GA_DOMAIN = os.environ.get('GA_DOMAIN', 'alienrank.com')

PHANTOM_OUT = os.path.join(LOG_ROOT, 'phantom-out.log')
PHANTOM_ERR = os.path.join(LOG_ROOT, 'phantom-err.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_ROOT, 'error.log'),
            'formatter': 'simple'
        }
        
    },
    'loggers': {
         'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'hvsite': {
            'handlers': ['file'],
            'level': 'DEBUG',
        }
    }
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']


TEMPLATE_VISIBLE_SETTINGS = (
    'GA_TRACKING_ID',
    'GA_DOMAIN',
    'ROOT_URL',
)

SERVER_EMAIL = "robot@alienrank.com"
DEFAULT_FROM_EMAIL = "AlienRank <robot@alienrank.com>"
#MANDRILL_API_KEY = ""
# A Test Key
# MANDRILL_API_KEY = "rtHSc0xZtHOLwWBSYs2nIg"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

CELERY_IMPORTS = (
    'rank.tasks',
)

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'read-reddit-top': {
        'task': 'rank.tasks.read_reddit_top',
        'schedule': timedelta(seconds=10),
    },
}

