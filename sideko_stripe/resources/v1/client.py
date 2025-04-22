from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.v1.climate import AsyncClimateClient, ClimateClient


class V1Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.climate = ClimateClient(base_client=self._base_client)


class AsyncV1Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.climate = AsyncClimateClient(base_client=self._base_client)
