from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.entitlement.active_entitlement import (
    ActiveEntitlementClient,
    AsyncActiveEntitlementClient,
)
from sideko_stripe.resources.entitlement.feature import (
    AsyncFeatureClient,
    FeatureClient,
)


class EntitlementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.active_entitlement = ActiveEntitlementClient(base_client=self._base_client)
        self.feature = FeatureClient(base_client=self._base_client)


class AsyncEntitlementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.active_entitlement = AsyncActiveEntitlementClient(
            base_client=self._base_client
        )
        self.feature = AsyncFeatureClient(base_client=self._base_client)
