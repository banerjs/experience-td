"""
Developement Django settings for the guidefinder project.
"""

from common import *
from os.path import join, normpath


## DEBUG CONFIGS ##
DEBUG = True
TEMPLATE_DEBUG = True


## DATABASE CONFIGS ##
DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personal',
        'USER': 'personal',
        'PASSWORD': 'a',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


## APP CONFIGS ##
INSTALLED_APPS += (
)


## STATIC AND MEDIA FILE CONFIGS ##
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
