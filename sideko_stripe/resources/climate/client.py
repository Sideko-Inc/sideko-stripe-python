from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.climate.order import AsyncOrderClient, OrderClient
from sideko_stripe.resources.climate.product import AsyncProductClient, ProductClient
from sideko_stripe.resources.climate.suppliers import (
    AsyncSuppliersClient,
    SuppliersClient,
)


class ClimateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.order = OrderClient(base_client=self._base_client)
        self.product = ProductClient(base_client=self._base_client)
        self.suppliers = SuppliersClient(base_client=self._base_client)


class AsyncClimateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.order = AsyncOrderClient(base_client=self._base_client)
        self.product = AsyncProductClient(base_client=self._base_client)
        self.suppliers = AsyncSuppliersClient(base_client=self._base_client)
