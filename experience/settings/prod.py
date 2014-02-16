"""
Prod Django settings for the guidefinder project.
"""

import os
import dj_database_url
from common import *

## MANAGER AND ADMIN SETTINGS ##
ADMINS = (("Siddhartha", 'banerjs.sid@gmail.com'),)
MANAGERS = ADMINS


## DATABASE SETTINGS ##
DATABASES = {
	'default': {
		'ENGINE': 'django_mongodb_engine',
		'NAME': 'app22270305',
		'USER': 'heroku',
		'PASSWORD': os.getenv('MONGODB_PWD'),
		'HOST': 'mongodb://heroku:3e994495838356bce8f3ff4ae6dafbcf@troup.mongohq.com/app22270305',
		'PORT': 10030,
	}
}


## HEROKU SETTINGS ##
# Honor the X-Forwarded-Proto header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


## APP CONFIGS ##
INSTALLED_APPS += (
)

## S3 CONFIGS ##
# Change default Django settings
DEFAULT_FILE_STORAGE = '{0}.libs.storages.utils.MediaRootS3BotoStorage'.format(BASE_NAME)
STATICFILES_STORAGE = '{0}.libs.storages.utils.StaticRootS3BotoStorage'.format(BASE_NAME)

# storages specific settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_PRELOAD_METADATA = True
AWS_STORAGE_BUCKET_NAME = 'experience-td'


## STATIC AND MEDIA FILES ##
# There are a bunch of configs here according to Heroku. However,
# I do not trust those changes. Let's keep using the current settings
# until I can tell for sure what's going on with the static files.
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/static/'
MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/media/'
