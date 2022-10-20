"""
Entitlements client for working with Daas entitlments API.
"""
from ..base_client import BaseClient
from ..service_base_client import ServiceBaseClient

class EntitlementsClient(ServiceBaseClient):
    """
    Client for working with Daas entitlements APIs.
    """
    
    def __init__(
        self, 
        client: BaseClient, 
        service_version: str = "1.0", 
        is_dev: bool = False
    ) -> None:
        """
        Setup the EntitlementsClient

        :param client: client to use for connection
        :param service_version (optional): service version defaults to '1.0'.
        """
        super().__init__(client, "entitlements", service_version, is_dev)

    def is_healthy(self) -> bool:
        """
        Returns health status of the API
        """
        response = self._client.get(self.api_url("/health-check/"))
        return response.status_code == 200