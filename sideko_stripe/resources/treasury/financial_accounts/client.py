from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.treasury.financial_accounts.feature import (
    AsyncFeatureClient,
    FeatureClient,
)


class FinancialAccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.feature = FeatureClient(base_client=self._base_client)


class AsyncFinancialAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.feature = AsyncFeatureClient(base_client=self._base_client)
