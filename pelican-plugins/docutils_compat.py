"""Restore docutils.utils.error_reporting for m.css on Docutils 0.22+.

Docutils 0.22 removed that module. m.css still imports it when Pelican loads
the m.code plugin. This plugin installs a small stand-in before that import.
"""

import sys
import types

import docutils.utils
from docutils.io import _locale_encoding, error_string


def _install():
    name = "docutils.utils.error_reporting"
    if name in sys.modules:
        return
    module = types.ModuleType(name)
    module.locale_encoding = _locale_encoding
    module.SafeString = str
    module.ErrorString = error_string
    sys.modules[name] = module
    docutils.utils.error_reporting = module


_install()


def register():
    pass
