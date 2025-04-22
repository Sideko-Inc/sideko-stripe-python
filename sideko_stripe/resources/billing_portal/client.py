from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.billing_portal.configuration import (
    AsyncConfigurationClient,
    ConfigurationClient,
)
from sideko_stripe.resources.billing_portal.session import (
    AsyncSessionClient,
    SessionClient,
)


class BillingPortalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.configuration = ConfigurationClient(base_client=self._base_client)
        self.session = SessionClient(base_client=self._base_client)


class AsyncBillingPortalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.configuration = AsyncConfigurationClient(base_client=self._base_client)
        self.session = AsyncSessionClient(base_client=self._base_client)
