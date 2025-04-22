from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.checkout.session import AsyncSessionClient, SessionClient


class CheckoutClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.session = SessionClient(base_client=self._base_client)


class AsyncCheckoutClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.session = AsyncSessionClient(base_client=self._base_client)
