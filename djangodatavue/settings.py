# flake8: noqa
from djangodatavue.settings_shared import *

try:
    from djangodatavue.local_settings import *
except ImportError:
    pass
