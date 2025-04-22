from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.forwarding.request import AsyncRequestClient, RequestClient


class ForwardingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.request = RequestClient(base_client=self._base_client)


class AsyncForwardingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.request = AsyncRequestClient(base_client=self._base_client)
