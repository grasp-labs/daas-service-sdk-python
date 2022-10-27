"""Basic credentials using username/password"""
import requests

from typing import Union, Dict

from .base_credential import DaasBaseCredential


class DaasBasicCredential(DaasBaseCredential):
    """Get token via basic authentification"""

    def __init__(
        self,
        username: str,
        password: str,
        token_endpoint: str,
    ) -> None:
        super().__init__()
        self._username = username
        self._password = password
        self._token_endpoint = token_endpoint

    def get_token(self, **kwargs) -> Union[str, None]:
        """
        return access token.
        """
        token = self._get_token()
        if "access_token" in token:
            return token["access_token"]

    def _get_token(self) -> Dict:
        """Get token from daas auth"""
        url = self._token_endpoint
        data = {
            "email": self._username,
            "password": self._password,
        }

        response = requests.post(url=url, data=data)

        return response.json()
