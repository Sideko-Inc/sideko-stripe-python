from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.radar.early_fraud_warning import (
    AsyncEarlyFraudWarningClient,
    EarlyFraudWarningClient,
)
from sideko_stripe.resources.radar.value_list import (
    AsyncValueListClient,
    ValueListClient,
)
from sideko_stripe.resources.radar.value_list_item import (
    AsyncValueListItemClient,
    ValueListItemClient,
)


class RadarClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.value_list_item = ValueListItemClient(base_client=self._base_client)
        self.value_list = ValueListClient(base_client=self._base_client)
        self.early_fraud_warning = EarlyFraudWarningClient(
            base_client=self._base_client
        )


class AsyncRadarClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.value_list_item = AsyncValueListItemClient(base_client=self._base_client)
        self.value_list = AsyncValueListClient(base_client=self._base_client)
        self.early_fraud_warning = AsyncEarlyFraudWarningClient(
            base_client=self._base_client
        )
