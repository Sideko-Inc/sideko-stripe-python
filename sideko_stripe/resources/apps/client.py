from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.apps.secret import AsyncSecretClient, SecretClient


class AppsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.secret = SecretClient(base_client=self._base_client)


class AsyncAppsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.secret = AsyncSecretClient(base_client=self._base_client)
