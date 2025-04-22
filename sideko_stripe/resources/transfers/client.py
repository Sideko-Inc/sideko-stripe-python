from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.transfers.reversal import (
    AsyncReversalClient,
    ReversalClient,
)


class TransfersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.reversal = ReversalClient(base_client=self._base_client)


class AsyncTransfersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.reversal = AsyncReversalClient(base_client=self._base_client)
