# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
from settings import *

# Static URL
STATIC_URL = '/static/'

# Static Root
STATIC_ROOT = ''

# Static DIRS
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),'static'),)

# Static finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
