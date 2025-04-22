from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.financial_connections.account import (
    AccountClient,
    AsyncAccountClient,
)
from sideko_stripe.resources.financial_connections.session import (
    AsyncSessionClient,
    SessionClient,
)
from sideko_stripe.resources.financial_connections.transaction import (
    AsyncTransactionClient,
    TransactionClient,
)


class FinancialConnectionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.account = AccountClient(base_client=self._base_client)
        self.session = SessionClient(base_client=self._base_client)
        self.transaction = TransactionClient(base_client=self._base_client)


class AsyncFinancialConnectionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.account = AsyncAccountClient(base_client=self._base_client)
        self.session = AsyncSessionClient(base_client=self._base_client)
        self.transaction = AsyncTransactionClient(base_client=self._base_client)
