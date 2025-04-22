from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.quotes.line_item import AsyncLineItemClient, LineItemClient


class QuotesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.line_item = LineItemClient(base_client=self._base_client)


class AsyncQuotesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.line_item = AsyncLineItemClient(base_client=self._base_client)
