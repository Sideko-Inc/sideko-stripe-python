from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.billing.alert import AlertClient, AsyncAlertClient
from sideko_stripe.resources.billing.credit_balance_summary import (
    AsyncCreditBalanceSummaryClient,
    CreditBalanceSummaryClient,
)
from sideko_stripe.resources.billing.credit_balance_transaction import (
    AsyncCreditBalanceTransactionClient,
    CreditBalanceTransactionClient,
)
from sideko_stripe.resources.billing.credit_grant import (
    AsyncCreditGrantClient,
    CreditGrantClient,
)
from sideko_stripe.resources.billing.meter import AsyncMeterClient, MeterClient
from sideko_stripe.resources.billing.meter_event import (
    AsyncMeterEventClient,
    MeterEventClient,
)
from sideko_stripe.resources.billing.meter_event_adjustment import (
    AsyncMeterEventAdjustmentClient,
    MeterEventAdjustmentClient,
)


class BillingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.alert = AlertClient(base_client=self._base_client)
        self.credit_balance_summary = CreditBalanceSummaryClient(
            base_client=self._base_client
        )
        self.credit_balance_transaction = CreditBalanceTransactionClient(
            base_client=self._base_client
        )
        self.credit_grant = CreditGrantClient(base_client=self._base_client)
        self.meter = MeterClient(base_client=self._base_client)
        self.meter_event_adjustment = MeterEventAdjustmentClient(
            base_client=self._base_client
        )
        self.meter_event = MeterEventClient(base_client=self._base_client)


class AsyncBillingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.alert = AsyncAlertClient(base_client=self._base_client)
        self.credit_balance_summary = AsyncCreditBalanceSummaryClient(
            base_client=self._base_client
        )
        self.credit_balance_transaction = AsyncCreditBalanceTransactionClient(
            base_client=self._base_client
        )
        self.credit_grant = AsyncCreditGrantClient(base_client=self._base_client)
        self.meter = AsyncMeterClient(base_client=self._base_client)
        self.meter_event_adjustment = AsyncMeterEventAdjustmentClient(
            base_client=self._base_client
        )
        self.meter_event = AsyncMeterEventClient(base_client=self._base_client)
