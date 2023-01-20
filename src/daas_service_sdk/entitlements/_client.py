"""
Entitlements client for working with Daas entitlments API.
"""
from typing import Dict, List

from ..base_client import BaseClient
from ..service_base_client import ServiceBaseClient


class EntitlementsClient(ServiceBaseClient):
    """
    Client for working with Daas entitlements APIs.
    """

    def __init__(
        self, client: BaseClient, service_version: str = "v1", is_dev: bool = False
    ) -> None:
        """
        Set up the EntitlementsClient

        :param client: client to use for connection
        :param service_version (optional): service version defaults to '1.0'.
        """
        super().__init__(client, "entitlements", service_version, is_dev)

    def is_healthy(self) -> bool:
        """
        Returns health status of the API
        """
        response = self._client.get(self.api_url("health-check/"))
        return response.status_code == 200

    def list_groups(self) -> List[Dict]:
        """
        List groups
        """
        response_json = self._client.get_returning_json(self.api_url("groups/"))
        return response_json

    def list_group_members(self, group: str) -> dict:
        """
        List members in a group
        :param group: The id of the group.
        """
        return self._client.get_returning_json(self.api_url(f"groups/{group}/members/"))

    def get_product(self, product_id):
        """
        Get info for a product.
        :param product_id: The id of the group.
        """
        return self._client.get_returning_json(self.api_url(f"products/{product_id}/"))

    def delete_product(self, product_id):
        """
        Get info for a product.
        :param product_id: The id of the group.
        """
        return self._client.delete(self.api_url(f"products/{product_id}/"))

    def list_products(self):
        """
        Get info for all products.
        """
        return self._client.get_returning_json(self.api_url(f"products/"))
