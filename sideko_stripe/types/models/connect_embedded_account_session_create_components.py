import pydantic

from .connect_embedded_account_config_claim import ConnectEmbeddedAccountConfigClaim
from .connect_embedded_base_config_claim import ConnectEmbeddedBaseConfigClaim
from .connect_embedded_financial_account_config_claim import (
    ConnectEmbeddedFinancialAccountConfigClaim,
)
from .connect_embedded_financial_account_transactions_config_claim import (
    ConnectEmbeddedFinancialAccountTransactionsConfigClaim,
)
from .connect_embedded_issuing_card_config_claim import (
    ConnectEmbeddedIssuingCardConfigClaim,
)
from .connect_embedded_issuing_cards_list_config_claim import (
    ConnectEmbeddedIssuingCardsListConfigClaim,
)
from .connect_embedded_payments_config_claim import ConnectEmbeddedPaymentsConfigClaim
from .connect_embedded_payouts_config import ConnectEmbeddedPayoutsConfig


class ConnectEmbeddedAccountSessionCreateComponents(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_management: ConnectEmbeddedAccountConfigClaim = pydantic.Field(
        alias="account_management",
    )
    account_onboarding: ConnectEmbeddedAccountConfigClaim = pydantic.Field(
        alias="account_onboarding",
    )
    balances: ConnectEmbeddedPayoutsConfig = pydantic.Field(
        alias="balances",
    )
    documents: ConnectEmbeddedBaseConfigClaim = pydantic.Field(
        alias="documents",
    )
    financial_account: ConnectEmbeddedFinancialAccountConfigClaim = pydantic.Field(
        alias="financial_account",
    )
    financial_account_transactions: ConnectEmbeddedFinancialAccountTransactionsConfigClaim = pydantic.Field(
        alias="financial_account_transactions",
    )
    issuing_card: ConnectEmbeddedIssuingCardConfigClaim = pydantic.Field(
        alias="issuing_card",
    )
    issuing_cards_list: ConnectEmbeddedIssuingCardsListConfigClaim = pydantic.Field(
        alias="issuing_cards_list",
    )
    notification_banner: ConnectEmbeddedAccountConfigClaim = pydantic.Field(
        alias="notification_banner",
    )
    payment_details: ConnectEmbeddedPaymentsConfigClaim = pydantic.Field(
        alias="payment_details",
    )
    payments: ConnectEmbeddedPaymentsConfigClaim = pydantic.Field(
        alias="payments",
    )
    payouts: ConnectEmbeddedPayoutsConfig = pydantic.Field(
        alias="payouts",
    )
    payouts_list: ConnectEmbeddedBaseConfigClaim = pydantic.Field(
        alias="payouts_list",
    )
    tax_registrations: ConnectEmbeddedBaseConfigClaim = pydantic.Field(
        alias="tax_registrations",
    )
    tax_settings: ConnectEmbeddedBaseConfigClaim = pydantic.Field(
        alias="tax_settings",
    )
