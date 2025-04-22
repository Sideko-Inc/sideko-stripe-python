import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_resource_financial_addresses_features import (
    TreasuryFinancialAccountsResourceFinancialAddressesFeatures,
)
from .treasury_financial_accounts_resource_inbound_transfers import (
    TreasuryFinancialAccountsResourceInboundTransfers,
)
from .treasury_financial_accounts_resource_outbound_payments import (
    TreasuryFinancialAccountsResourceOutboundPayments,
)
from .treasury_financial_accounts_resource_outbound_transfers import (
    TreasuryFinancialAccountsResourceOutboundTransfers,
)
from .treasury_financial_accounts_resource_toggle_settings import (
    TreasuryFinancialAccountsResourceToggleSettings,
)


class TreasuryFinancialAccountFeatures(pydantic.BaseModel):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_issuing: typing.Optional[TreasuryFinancialAccountsResourceToggleSettings] = (
        pydantic.Field(alias="card_issuing", default=None)
    )
    """
    Toggle settings for enabling/disabling a feature
    """
    deposit_insurance: typing.Optional[
        TreasuryFinancialAccountsResourceToggleSettings
    ] = pydantic.Field(alias="deposit_insurance", default=None)
    """
    Toggle settings for enabling/disabling a feature
    """
    financial_addresses: typing.Optional[
        TreasuryFinancialAccountsResourceFinancialAddressesFeatures
    ] = pydantic.Field(alias="financial_addresses", default=None)
    """
    Settings related to Financial Addresses features on a Financial Account
    """
    inbound_transfers: typing.Optional[
        TreasuryFinancialAccountsResourceInboundTransfers
    ] = pydantic.Field(alias="inbound_transfers", default=None)
    """
    InboundTransfers contains inbound transfers features for a FinancialAccount.
    """
    intra_stripe_flows: typing.Optional[
        TreasuryFinancialAccountsResourceToggleSettings
    ] = pydantic.Field(alias="intra_stripe_flows", default=None)
    """
    Toggle settings for enabling/disabling a feature
    """
    object: typing_extensions.Literal["treasury.financial_account_features"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    outbound_payments: typing.Optional[
        TreasuryFinancialAccountsResourceOutboundPayments
    ] = pydantic.Field(alias="outbound_payments", default=None)
    """
    Settings related to Outbound Payments features on a Financial Account
    """
    outbound_transfers: typing.Optional[
        TreasuryFinancialAccountsResourceOutboundTransfers
    ] = pydantic.Field(alias="outbound_transfers", default=None)
    """
    OutboundTransfers contains outbound transfers features for a FinancialAccount.
    """
