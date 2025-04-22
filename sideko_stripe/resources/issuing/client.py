from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.issuing.authorization import (
    AsyncAuthorizationClient,
    AuthorizationClient,
)
from sideko_stripe.resources.issuing.card import AsyncCardClient, CardClient
from sideko_stripe.resources.issuing.cardholder import (
    AsyncCardholderClient,
    CardholderClient,
)
from sideko_stripe.resources.issuing.dispute import AsyncDisputeClient, DisputeClient
from sideko_stripe.resources.issuing.personalization_design import (
    AsyncPersonalizationDesignClient,
    PersonalizationDesignClient,
)
from sideko_stripe.resources.issuing.physical_bundle import (
    AsyncPhysicalBundleClient,
    PhysicalBundleClient,
)
from sideko_stripe.resources.issuing.settlement import (
    AsyncSettlementClient,
    SettlementClient,
)
from sideko_stripe.resources.issuing.token import AsyncTokenClient, TokenClient
from sideko_stripe.resources.issuing.transaction import (
    AsyncTransactionClient,
    TransactionClient,
)


class IssuingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.authorization = AuthorizationClient(base_client=self._base_client)
        self.cardholder = CardholderClient(base_client=self._base_client)
        self.card = CardClient(base_client=self._base_client)
        self.dispute = DisputeClient(base_client=self._base_client)
        self.personalization_design = PersonalizationDesignClient(
            base_client=self._base_client
        )
        self.physical_bundle = PhysicalBundleClient(base_client=self._base_client)
        self.settlement = SettlementClient(base_client=self._base_client)
        self.token = TokenClient(base_client=self._base_client)
        self.transaction = TransactionClient(base_client=self._base_client)


class AsyncIssuingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.authorization = AsyncAuthorizationClient(base_client=self._base_client)
        self.cardholder = AsyncCardholderClient(base_client=self._base_client)
        self.card = AsyncCardClient(base_client=self._base_client)
        self.dispute = AsyncDisputeClient(base_client=self._base_client)
        self.personalization_design = AsyncPersonalizationDesignClient(
            base_client=self._base_client
        )
        self.physical_bundle = AsyncPhysicalBundleClient(base_client=self._base_client)
        self.settlement = AsyncSettlementClient(base_client=self._base_client)
        self.token = AsyncTokenClient(base_client=self._base_client)
        self.transaction = AsyncTransactionClient(base_client=self._base_client)
