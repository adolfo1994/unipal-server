from settings_base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'unipal',
        'USER': 'unipal',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# ----------------- BEGIN DEVELOPMENT PARAMETERS -----------------
# Please set this parameters only for development

LANGUAGE_CODE = 'en-us'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'default': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    },
}
