import os
from requests.exceptions import HTTPError

from daas_service_sdk.credentials import DaasBasicCredential
from daas_service_sdk.base_client import BaseClient
from daas_service_sdk.entitlements import EntitlementsClient


def main():
    """
    Example code for calling daas entitlements service endpoint.
    """

    cred = DaasBasicCredential(
        username=os.environ.get("username"),
        password=os.environ.get("password"),
        token_endpoint="https://auth-dev.grasp-daas.com/rest-auth/login/",
    )
    client = BaseClient(server_url="https://grasp-daas.com/", credential=cred)

    entitlements_client = EntitlementsClient(client=client, is_dev=True)

    try:
        print(entitlements_client.list_products())
    except HTTPError as exc:
        print(exc.response, exc.response.content)


if __name__ == "__main__":
    main()
