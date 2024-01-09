from .base import *

THIRD_PARTY_APPS = ['debug_toolbar']

DEBUG = config('DEBUG')

INSTALLED_APPS += THIRD_PARTY_APPS

THIRT_PARTY_MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware']

MIDDLEWARE += THIRT_PARTY_MIDDLEWARE

DATABASES={
    "default":{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INTERNAL_IPS=[
    '127.0.0.1',
]