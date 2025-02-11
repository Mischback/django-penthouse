# SPDX-FileCopyrightText: 2024 Mischback
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

# Django imports
from django.utils.translation import gettext_noop as _

# local imports
from .settings_test import *

INSTALLED_APPS += [
    "debug_toolbar",
]

# Enable Django's DEBUG mode
DEBUG = True

# Re-enable Internationalization (turned off iin settings_test.py)
USE_I18N = True

# enable Localization
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True

LANGUAGES = (("en", _("English")), ("de", _("German")))

MIDDLEWARE += [
    # add DebugToolbar middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Inject the localization middleware into the right position
MIDDLEWARE = [
    y
    for i, x in enumerate(MIDDLEWARE)
    for y in (
        ("django.middleware.locale.LocaleMiddleware", x)
        if MIDDLEWARE[i - 1] == "django.contrib.sessions.middleware.SessionMiddleware"
        else (x,)
    )
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "dev_f": {
            "format": "[%(levelname)s] %(name)s:%(lineno)d:%(funcName)s \n\t %(message)s",
        },
    },
    "handlers": {
        "def_h": {
            "class": "logging.StreamHandler",
            "formatter": "dev_f",
        },
    },
    "loggers": {
        "penthouse": {
            "handlers": ["def_h"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "tests.util.callback_show_debug_toolbar",
}
