"""Tests settings"""

SECRET_KEY = 'secret-key'

DATABASES = {
    'default': {
        'NAME': 'tagging.db',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'tagging',
    'tagging.tests',
]
