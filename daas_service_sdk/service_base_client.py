"""
DaaS Service client base.
"""
from urllib.parse import urljoin

from .base_client import BaseClient


class ServiceBaseClient:
    """
    Abstract base service client class for connecting with Daas Platform.
    Not intended to be used directly, rather one of its subclasses.
    """

    def __init__(
        self,
        client: BaseClient,
        service_name: str,
        service_version: str = "1.0",
        is_dev: bool = False,
    ) -> None:
        """
        Setup the service base client.

        :param client: client to use for connection.
        :param service_name: service name.
        :service version: service version, default is 1.0. NB. mabye should use 'latest'
        :is_dev: true for dev version
        """
        if not client or not isinstance(client, BaseClient):
            raise ValueError("Client should be an BaseClient instance.")

        self._client = client
        self._service_name = service_name
        self._service_version = service_version
        self._is_dev = is_dev

    @property
    def service_name(self) -> str:
        """
        Get name of the service.

        By default, used for constructing the url unless api_url is overwridden.
        """
        return self._service_name

    @property
    def service_version(self) -> str:
        """
        Version of the api being used
        """
        return self._service_version

    def api_url(self, extra_path: str = None) -> str:
        """
        Get a url for the api including any specified extra path

        :param extra_path: extra path to add to the base url. Defaults to None.
        """
        if self._is_dev:
            url = urljoin(
                self._client.server_url,
                f"/api/{self.service_name}-dev/{self.service_version}/",
            )
        else:
            url = urljoin(
                self._client.server_url,
                f"/api/{self.service_name}/{self.service_version}/",
            )

        if extra_path:
            url = urljoin(url, extra_path)

        return url
