from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.sigma.scheduled_query_run import (
    AsyncScheduledQueryRunClient,
    ScheduledQueryRunClient,
)


class SigmaClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.scheduled_query_run = ScheduledQueryRunClient(
            base_client=self._base_client
        )


class AsyncSigmaClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.scheduled_query_run = AsyncScheduledQueryRunClient(
            base_client=self._base_client
        )
