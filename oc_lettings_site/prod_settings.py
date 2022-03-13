from .settings import *

DEBUG = False

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

SECRET_KEY = get_var('SECRET_KEY', os.getenv('SECRET_KEY'))

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ocletting8.herokuapp.com']