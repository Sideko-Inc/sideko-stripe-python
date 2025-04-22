from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.tax.calculations.line_item import (
    AsyncLineItemClient,
    LineItemClient,
)


class CalculationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.line_item = LineItemClient(base_client=self._base_client)


class AsyncCalculationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.line_item = AsyncLineItemClient(base_client=self._base_client)
