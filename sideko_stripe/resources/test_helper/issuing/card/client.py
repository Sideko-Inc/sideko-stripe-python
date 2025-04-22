from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.test_helper.issuing.card.shipping import (
    AsyncShippingClient,
    ShippingClient,
)


class CardClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.shipping = ShippingClient(base_client=self._base_client)


class AsyncCardClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.shipping = AsyncShippingClient(base_client=self._base_client)
