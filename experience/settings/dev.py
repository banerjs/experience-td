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
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'experience_db',
    }
}


## APP CONFIGS ##
INSTALLED_APPS += (
)

TEMPLATE_CONTEXT_PROCESSORS += (
	"experience.libs.processors.context.include_settings",
)


## STATIC AND MEDIA FILE CONFIGS ##
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
