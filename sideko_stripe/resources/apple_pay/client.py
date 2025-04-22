from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.apple_pay.domain import AsyncDomainClient, DomainClient


class ApplePayClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.domain = DomainClient(base_client=self._base_client)


class AsyncApplePayClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.domain = AsyncDomainClient(base_client=self._base_client)
