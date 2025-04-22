import pydantic
import typing
import typing_extensions

from .treasury_financial_account_features import TreasuryFinancialAccountFeatures
from .treasury_financial_account_metadata import TreasuryFinancialAccountMetadata
from .treasury_financial_accounts_resource_balance import (
    TreasuryFinancialAccountsResourceBalance,
)
from .treasury_financial_accounts_resource_financial_address import (
    TreasuryFinancialAccountsResourceFinancialAddress,
)
from .treasury_financial_accounts_resource_platform_restrictions import (
    TreasuryFinancialAccountsResourcePlatformRestrictions,
)
from .treasury_financial_accounts_resource_status_details import (
    TreasuryFinancialAccountsResourceStatusDetails,
)


class TreasuryFinancialAccount(pydantic.BaseModel):
    """
    Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.
    FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active_features: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "financial_addresses.aba.forwarding",
                "inbound_transfers.ach",
                "intra_stripe_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ] = pydantic.Field(alias="active_features", default=None)
    """
    The array of paths to active Features in the Features hash.
    """
    balance: TreasuryFinancialAccountsResourceBalance = pydantic.Field(
        alias="balance",
    )
    """
    Balance information for the FinancialAccount
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    features: typing.Optional[TreasuryFinancialAccountFeatures] = pydantic.Field(
        alias="features", default=None
    )
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """
    financial_addresses: typing.List[
        TreasuryFinancialAccountsResourceFinancialAddress
    ] = pydantic.Field(
        alias="financial_addresses",
    )
    """
    The set of credentials that resolve to a FinancialAccount.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    is_default: typing.Optional[bool] = pydantic.Field(alias="is_default", default=None)
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[TreasuryFinancialAccountMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    """
    The nickname for the FinancialAccount.
    """
    object: typing_extensions.Literal["treasury.financial_account"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending_features: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "financial_addresses.aba.forwarding",
                "inbound_transfers.ach",
                "intra_stripe_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ] = pydantic.Field(alias="pending_features", default=None)
    """
    The array of paths to pending Features in the Features hash.
    """
    platform_restrictions: typing.Optional[
        TreasuryFinancialAccountsResourcePlatformRestrictions
    ] = pydantic.Field(alias="platform_restrictions", default=None)
    """
    Restrictions that a Connect Platform has placed on this FinancialAccount.
    """
    restricted_features: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "financial_addresses.aba.forwarding",
                "inbound_transfers.ach",
                "intra_stripe_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ] = pydantic.Field(alias="restricted_features", default=None)
    """
    The array of paths to restricted Features in the Features hash.
    """
    status: typing_extensions.Literal["closed", "open"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this FinancialAccount.
    """
    status_details: TreasuryFinancialAccountsResourceStatusDetails = pydantic.Field(
        alias="status_details",
    )
    supported_currencies: typing.List[str] = pydantic.Field(
        alias="supported_currencies",
    )
    """
    The currencies the FinancialAccount can hold a balance in. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.
    """
