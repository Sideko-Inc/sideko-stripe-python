from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.tax.calculation import (
    AsyncCalculationClient,
    CalculationClient,
)
from sideko_stripe.resources.tax.calculations import (
    AsyncCalculationsClient,
    CalculationsClient,
)
from sideko_stripe.resources.tax.registration import (
    AsyncRegistrationClient,
    RegistrationClient,
)
from sideko_stripe.resources.tax.setting import AsyncSettingClient, SettingClient
from sideko_stripe.resources.tax.transaction import (
    AsyncTransactionClient,
    TransactionClient,
)


class TaxClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.calculation = CalculationClient(base_client=self._base_client)
        self.calculations = CalculationsClient(base_client=self._base_client)
        self.registration = RegistrationClient(base_client=self._base_client)
        self.setting = SettingClient(base_client=self._base_client)
        self.transaction = TransactionClient(base_client=self._base_client)


class AsyncTaxClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.calculation = AsyncCalculationClient(base_client=self._base_client)
        self.calculations = AsyncCalculationsClient(base_client=self._base_client)
        self.registration = AsyncRegistrationClient(base_client=self._base_client)
        self.setting = AsyncSettingClient(base_client=self._base_client)
        self.transaction = AsyncTransactionClient(base_client=self._base_client)
