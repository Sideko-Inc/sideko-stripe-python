from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.test_helper.confirmation_token import (
    AsyncConfirmationTokenClient,
    ConfirmationTokenClient,
)
from sideko_stripe.resources.test_helper.customer import (
    AsyncCustomerClient,
    CustomerClient,
)
from sideko_stripe.resources.test_helper.issuing import (
    AsyncIssuingClient,
    IssuingClient,
)
from sideko_stripe.resources.test_helper.refund import AsyncRefundClient, RefundClient
from sideko_stripe.resources.test_helper.terminal import (
    AsyncTerminalClient,
    TerminalClient,
)
from sideko_stripe.resources.test_helper.test_clock import (
    AsyncTestClockClient,
    TestClockClient,
)
from sideko_stripe.resources.test_helper.treasury import (
    AsyncTreasuryClient,
    TreasuryClient,
)


class TestHelperClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.test_clock = TestClockClient(base_client=self._base_client)
        self.confirmation_token = ConfirmationTokenClient(base_client=self._base_client)
        self.customer = CustomerClient(base_client=self._base_client)
        self.issuing = IssuingClient(base_client=self._base_client)
        self.refund = RefundClient(base_client=self._base_client)
        self.terminal = TerminalClient(base_client=self._base_client)
        self.treasury = TreasuryClient(base_client=self._base_client)


class AsyncTestHelperClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.test_clock = AsyncTestClockClient(base_client=self._base_client)
        self.confirmation_token = AsyncConfirmationTokenClient(
            base_client=self._base_client
        )
        self.customer = AsyncCustomerClient(base_client=self._base_client)
        self.issuing = AsyncIssuingClient(base_client=self._base_client)
        self.refund = AsyncRefundClient(base_client=self._base_client)
        self.terminal = AsyncTerminalClient(base_client=self._base_client)
        self.treasury = AsyncTreasuryClient(base_client=self._base_client)
