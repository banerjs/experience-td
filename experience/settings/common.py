"""
Common Django settings for guidefinder project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import sys
import os
from os.path import abspath, basename, dirname, join, normpath


## RUNTIME CONFIGS ##
# Make sure that the runtime environment is available to all the apps
RUNTIME_ENV = os.getenv('RUNTIME_ENV')


## PATH CONFIGS ##
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(__file__)))
BASE_NAME = 'experience'


## DEBUG CONFIGS ##
# Disable Debugging by default
DEBUG = False
TEMPLATE_DEBUG = False


## GENERAL CONFIGS ##
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


## MEDIA AND STATIC FILE CONFIGS ##
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT_NAME = 'static'
MEDIA_ROOT_NAME = 'media'
TEMPLATE_ROOT_NAME = 'templates'

STATICFILES_DIRS = (
    normpath(join(BASE_DIR, STATIC_ROOT_NAME)),
)


## TEMPLATE CONFIGS ##
TEMPLATE_DIRS = (
	normpath(join(BASE_DIR, 'templates')),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


## MIDDLEWARE CONFIGS ##
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


## APP CONFIGS ##
INSTALLED_APPS = (
    # Django Default Apps
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'storages',
    'collectfast',

    # Project specific apps
    'experience.apps.articles',
)

ROOT_URLCONF = '{0}.urls'.format(BASE_NAME)

WSGI_APPLICATION = '{0}.wsgi.application'.format(BASE_NAME)


## SECRET KEY CONFIG ##
# Get the SECRET_KEY from the environment variables
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
