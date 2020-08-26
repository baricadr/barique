from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests

from baricadr.exceptions import BaricadrConnectionError, BaricadrApiError

from future import standard_library

standard_library.install_aliases()

class Client(object):
    """
    Base client class implementing methods to make queries to the server
    """

    def __init__(self, host, port):
        self.host = host
        self.port = str(port)

    def _api_call(self, call_type, endpoint, body={}):

        url = "http://{}:{}{}".format(self.host, self.port, endpoint)

        try:
            if call_type == "get":
                r = requests.get(url, json=body)
            elif call_type == "post":
                r = requests.post(url, json=body)

            if r.status_code == "400":
                raise BaricadrApiError("API call returned the following error: '{}'".format(r.json()['error']))
            elif r.status_code == "502":
                raise BaricadrApiError("Unknown server error")
            else:
                return r.json()

        except requests.exceptions.RequestException:
            raise BaricadrConnectionError("Cannot connect to {}:{}. Please check the connection.".format(self.host,self.port))
