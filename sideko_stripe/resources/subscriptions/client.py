from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.subscriptions.discount import (
    AsyncDiscountClient,
    DiscountClient,
)


class SubscriptionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.discount = DiscountClient(base_client=self._base_client)


class AsyncSubscriptionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.discount = AsyncDiscountClient(base_client=self._base_client)
