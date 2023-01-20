"""
Base client to daas service apis
"""

import logging
import requests

from typing import Union, Dict, List
from requests import Response, HTTPError

from .credentials import DaasBaseCredential

logger = logging.getLogger(__name__)


class BaseClient:
    """
    Class for connecting with APIs.
    """

    def __init__(
        self,
        server_url: str,
        credential: DaasBaseCredential,
    ):
        """
        Setup the new client
        :param server_url: url of the server without any path e.g. https://www.test.com
        :param credential: credentials used for connection
        """
        self._server_url = server_url
        self._credential = credential

    @property
    def server_url(self) -> str:
        """Url of the API server"""
        return self._server_url

    @property
    def credential(self) -> str:
        """Credentials used for connection"""
        return self._credential

    def get_headers(self):
        """
        Get needed http headers, including authorization bearer token.
        Raises:
            NotImplementedError: Should be implemented by subclasses.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._credential.get_token()}",
        }

    def get(self, url: str, ok_status_codes: List = None) -> Response:
        """GET from the specified url
        :param url: url to GET from to
        :param ok_status_codes: list of status code indicating success
        Raises:
            HTTPError: Raised if ok_status_codes are passed and the get returns a different status
        """
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if ok_status_codes is not None and response.status_code not in ok_status_codes:
            raise HTTPError(response=response)
        return response

    def delete(self, url: str, ok_status_codes: List = None) -> Response:
        """GET from the specified url
        :param url: url to GET from to
        :param ok_status_codes: list of status code indicating success
        Raises:
            HTTPError: Raised if ok_status_codes are passed and the get returns a different status
        """
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        if ok_status_codes is not None and response.status_code not in ok_status_codes:
            raise HTTPError(response=response)
        return response

    def get_returning_json(self, url: str, ok_status_codes: list = None) -> Dict:
        """
        Get data from the specified url in json format.
        To be able to do a conversion to json we typically need a valid http response so
        pass this in ok_status_codes.
        :param url: url to GET from to
        :param ok_status_codes: list of status code indicating success. Defaults to [200].
        Raises:
            HTTPError: Raised if the get returns a status other than those in ok_status_codes
        """
        if ok_status_codes is None:
            ok_status_codes = [200]
        response = self.get(url, ok_status_codes)
        return response.json()

    def post(
        self, url: str, data: Union[str, Dict], ok_status_codes: List = None
    ) -> Response:
        """
        POST data to the specified url

        :param url: url to POST to
        :param data: json data as string or dict to send as the body
        :param ok_status_codes: list of status code indicating success

        Raises:
            HTTPError: Raised if ok_status_codes are passed and the post returns a different status
        """
        headers = self.get_headers()

        # determine whether to send to requests as data or json
        _json = None
        if isinstance(data, Dict):
            _json = data
            data = None

        response = requests.post(url, data=data, json=_json, headers=headers)
        if ok_status_codes is not None and response.status_code not in ok_status_codes:
            raise HTTPError(response=response)
        return response

    def post_returning_json(
        self, url: str, data: Union[str, Dict], ok_status_codes: list = None
    ) -> Dict:
        """
        Post data to the specified url and get the result in json format.

        To be able to do a conversion to json we typically need a valid http response so
        pass this in ok_status_codes.

        :param url: url to POST to
        :param data: json data as string or dict to send as the body
        :param ok_status_codes: Status codes indicating successful call. Defaults to [200].

        Raises:
            HTTPError: Raised if the get returns a status other than those in ok_status_codes
        """
        if ok_status_codes is None:
            ok_status_codes = [200]
        response = self.post(url, data, ok_status_codes)
        return response.json()
