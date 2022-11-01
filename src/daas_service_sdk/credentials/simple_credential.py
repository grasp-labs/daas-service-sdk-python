"""Simple credential with token directly"""
from .base_credential import DaasBaseCredential


class SimpleCredential(DaasBaseCredential):
    """
    Simple credentials by passing token directly to daas client.
    """

    def __init__(self, token: str):
        self._token = token

    def get_token(self, **kwargs) -> str:
        return self._token
