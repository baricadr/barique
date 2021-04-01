from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from baricadr.exceptions import BaricadrApiError, BaricadrConnectionError, BaricadrNotImplementedError

from future import standard_library

import requests

standard_library.install_aliases()


class Client(object):
    """
    Base client class implementing methods to make queries to the server
    """

    def __init__(self, url, login, password, endpoints):
        self.url = url
        self.login = login
        self.password = password
        self.endpoints = endpoints

    def _api_call(self, call_type, endpoint_name, body={}):

        url = self._format_url(call_type, endpoint_name, body)

        auth = None
        if self.login and self.password:
            auth = (self.login, self.password)

        try:
            if call_type == "get":
                r = requests.get(url, json=body, auth=auth)
            elif call_type == "post":
                r = requests.post(url, json=body, auth=auth)

            if r.status_code == 400:
                raise BaricadrApiError("API call returned the following error: '{}'".format(r.json()['error']))
            elif r.status_code == 502:
                raise BaricadrApiError("Unknown server error")
            else:
                return r.json()

        except requests.exceptions.RequestException:
            raise BaricadrConnectionError("Cannot connect to {}. Please check the connection.".format(self.url))

    def _format_url(self, call_type, endpoint_name, body):

        endpoint = self.endpoints.get(endpoint_name)
        if not endpoint:
            raise BaricadrNotImplementedError()

        # Fill parameters in the url
        if call_type == "get":
            groups = re.findall(r'<(.*?)>', endpoint)
            for group in groups:
                if group not in body:
                    raise BaricadrApiError("Missing get parameter " + group)
                endpoint = endpoint.replace("<{}>".format(group), body.get(group))

        return "{}{}".format(self.url, endpoint)
