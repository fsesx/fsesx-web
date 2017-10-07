# -*- coding: utf-8 -*-
"""
    settings.production
    ~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by The FSE Stock Exchange Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from .base import BASE_DIR
from .base import SECRET_KEY
from .base import ALLOWED_HOSTS
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import ROOT_URLCONF
from .base import TEMPLATES
from .base import WSGI_APPLICATION
from .base import DATABASES
from .base import AUTH_PASSWORD_VALIDATORS
from .base import LANGUAGE_CODE
from .base import TIME_ZONE
from .base import USE_I18N
from .base import USE_L10N
from .base import USE_TZ
from .base import STATIC_ROOT
from .base import STATIC_URL
from .base import STATICFILES_DIRS
from .base import STATICFILES_STORAGE

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False
