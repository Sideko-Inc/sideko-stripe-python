from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.test_helper.treasury.inbound_transfers import (
    AsyncInboundTransfersClient,
    InboundTransfersClient,
)
from sideko_stripe.resources.test_helper.treasury.outbound_payment import (
    AsyncOutboundPaymentClient,
    OutboundPaymentClient,
)
from sideko_stripe.resources.test_helper.treasury.outbound_transfer import (
    AsyncOutboundTransferClient,
    OutboundTransferClient,
)
from sideko_stripe.resources.test_helper.treasury.received_credit import (
    AsyncReceivedCreditClient,
    ReceivedCreditClient,
)
from sideko_stripe.resources.test_helper.treasury.received_debit import (
    AsyncReceivedDebitClient,
    ReceivedDebitClient,
)


class TreasuryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.inbound_transfers = InboundTransfersClient(base_client=self._base_client)
        self.outbound_payment = OutboundPaymentClient(base_client=self._base_client)
        self.outbound_transfer = OutboundTransferClient(base_client=self._base_client)
        self.received_credit = ReceivedCreditClient(base_client=self._base_client)
        self.received_debit = ReceivedDebitClient(base_client=self._base_client)


class AsyncTreasuryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.inbound_transfers = AsyncInboundTransfersClient(
            base_client=self._base_client
        )
        self.outbound_payment = AsyncOutboundPaymentClient(
            base_client=self._base_client
        )
        self.outbound_transfer = AsyncOutboundTransferClient(
            base_client=self._base_client
        )
        self.received_credit = AsyncReceivedCreditClient(base_client=self._base_client)
        self.received_debit = AsyncReceivedDebitClient(base_client=self._base_client)
