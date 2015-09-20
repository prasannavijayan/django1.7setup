# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Import Settings
from settings import *

#environment variable
environment = "production"  # Use production or staging

# Important Secret Key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xm_b%5q5g4ll6pqjz%p+2nr(blkhu2t9np8u30f3@7r=pxut-)'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Production
if environment == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    DEBUG = False

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = []
