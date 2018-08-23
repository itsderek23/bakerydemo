from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

SCOUT_NAME = SCOUT_NAME + " [DEV]"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stdout': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z',
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'stdout',
        },
        'scout_apm': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'scout_apm_debug.log',
        },
    },
    'root': {
        'handlers': ['stdout'],
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
    },
    'loggers': {
        'scout_apm': {
            'handlers': ['scout_apm'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
