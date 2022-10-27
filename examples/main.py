from daas_service_sdk.credentials import DaasBasicCredential
from daas_service_sdk.base_client import BaseClient
from daas_service_sdk.entitlements import EntitlementsClient


def main():
    """
    Example code for calling daas entitlements service endpoint.
    """

    cred = DaasBasicCredential(
        username="",
        password="",
        token_endpoint="https://auth-dev.grasp-daas.com/rest-auth/login/",
    )
    # print(cred.get_token())

    client = BaseClient(server_url="https://grasp-daas.com/", credential=cred)

    entitlements_client = EntitlementsClient(client=client, is_dev=True)

    print(entitlements_client.is_healthy())
    print(entitlements_client.list_groups())


if __name__ == "__main__":
    main()
