from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.treasury.credit_reversal import (
    AsyncCreditReversalClient,
    CreditReversalClient,
)
from sideko_stripe.resources.treasury.debit_reversal import (
    AsyncDebitReversalClient,
    DebitReversalClient,
)
from sideko_stripe.resources.treasury.financial_account import (
    AsyncFinancialAccountClient,
    FinancialAccountClient,
)
from sideko_stripe.resources.treasury.financial_accounts import (
    AsyncFinancialAccountsClient,
    FinancialAccountsClient,
)
from sideko_stripe.resources.treasury.inbound_transfer import (
    AsyncInboundTransferClient,
    InboundTransferClient,
)
from sideko_stripe.resources.treasury.outbound_payment import (
    AsyncOutboundPaymentClient,
    OutboundPaymentClient,
)
from sideko_stripe.resources.treasury.outbound_transfer import (
    AsyncOutboundTransferClient,
    OutboundTransferClient,
)
from sideko_stripe.resources.treasury.received_credit import (
    AsyncReceivedCreditClient,
    ReceivedCreditClient,
)
from sideko_stripe.resources.treasury.received_debit import (
    AsyncReceivedDebitClient,
    ReceivedDebitClient,
)
from sideko_stripe.resources.treasury.transaction import (
    AsyncTransactionClient,
    TransactionClient,
)
from sideko_stripe.resources.treasury.transaction_entry import (
    AsyncTransactionEntryClient,
    TransactionEntryClient,
)


class TreasuryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.credit_reversal = CreditReversalClient(base_client=self._base_client)
        self.debit_reversal = DebitReversalClient(base_client=self._base_client)
        self.financial_account = FinancialAccountClient(base_client=self._base_client)
        self.financial_accounts = FinancialAccountsClient(base_client=self._base_client)
        self.inbound_transfer = InboundTransferClient(base_client=self._base_client)
        self.outbound_payment = OutboundPaymentClient(base_client=self._base_client)
        self.outbound_transfer = OutboundTransferClient(base_client=self._base_client)
        self.received_credit = ReceivedCreditClient(base_client=self._base_client)
        self.received_debit = ReceivedDebitClient(base_client=self._base_client)
        self.transaction_entry = TransactionEntryClient(base_client=self._base_client)
        self.transaction = TransactionClient(base_client=self._base_client)


class AsyncTreasuryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.credit_reversal = AsyncCreditReversalClient(base_client=self._base_client)
        self.debit_reversal = AsyncDebitReversalClient(base_client=self._base_client)
        self.financial_account = AsyncFinancialAccountClient(
            base_client=self._base_client
        )
        self.financial_accounts = AsyncFinancialAccountsClient(
            base_client=self._base_client
        )
        self.inbound_transfer = AsyncInboundTransferClient(
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
        self.transaction_entry = AsyncTransactionEntryClient(
            base_client=self._base_client
        )
        self.transaction = AsyncTransactionClient(base_client=self._base_client)
