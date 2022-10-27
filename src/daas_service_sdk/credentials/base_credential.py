from abc import ABC, abstractmethod


class DaasBaseCredential(ABC):
    """
    Abstract base credential class for connecting with Daas service.
    Cannot be used directly.
    """

    @abstractmethod
    def get_token(self, **kwargs) -> str:
        """Get access token, trying to refresh if needed."""
