from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.v1.climate.suppliers import (
    AsyncSuppliersClient,
    SuppliersClient,
)


class ClimateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.suppliers = SuppliersClient(base_client=self._base_client)


class AsyncClimateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.suppliers = AsyncSuppliersClient(base_client=self._base_client)
