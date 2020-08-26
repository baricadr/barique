from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()


class BaricadrConnectionError(Exception):
    """Raised when the connection to the Barricadr server fails"""

class BaricadrEndpointError(Exception):
    """Raised when the API returns an error"""
