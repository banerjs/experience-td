# This file provides utility functions that extend the storage modules in use
# with Django at the moment

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

# Storage backends for static and media files

StaticRootS3BotoStorage = lambda: S3BotoStorage(location=settings.STATIC_ROOT_NAME)
MediaRootS3BotoStorage = lambda: S3BotoStorage(location=settings.MEDIA_ROOT_NAME)
