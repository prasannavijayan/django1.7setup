# Application definition
# Donot modify the INSTALLED_APPS until you are aware of what you are doing.
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
)

# OUR_APPS
OUR_APPS = (
    'website',
)

INSTALLED_APPS += OUR_APPS;
