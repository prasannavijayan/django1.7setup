# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Import Settings
from settings import *

#environment variable
environment = "development"  # Use production or staging

# Important Secret Key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xm_b%5q5g4ll6pqjz%p+2nr(blkhu2t9np8u30f3@7r=pxut-)'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Development
if environment == "development":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []
