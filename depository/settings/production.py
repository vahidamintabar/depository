from .base import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/home/khat/db/db.sqlite3'),  # NOQA
    }
}
