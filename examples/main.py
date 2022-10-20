from daas_service_sdk.base_client import BaseClient
from daas_service_sdk.entitlements import EntitlementsClient


def main():
    """
    Example code for calling daas entitlements service endpoint.
    """
    token = ""
    client = BaseClient(server_url="https://grasp-daas.com/", token=token)

    entitlements_client = EntitlementsClient(client=client, is_dev=True)

    print(entitlements_client.is_healthy())
    print(entitlements_client.list_groups())


if __name__ == "__main__":
    main()
