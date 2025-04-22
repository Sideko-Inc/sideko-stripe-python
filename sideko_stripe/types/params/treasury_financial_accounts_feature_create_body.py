import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_feature_create_body_card_issuing import (
    TreasuryFinancialAccountsFeatureCreateBodyCardIssuing,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyCardIssuing,
)
from .treasury_financial_accounts_feature_create_body_deposit_insurance import (
    TreasuryFinancialAccountsFeatureCreateBodyDepositInsurance,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyDepositInsurance,
)
from .treasury_financial_accounts_feature_create_body_financial_addresses import (
    TreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses,
)
from .treasury_financial_accounts_feature_create_body_inbound_transfers import (
    TreasuryFinancialAccountsFeatureCreateBodyInboundTransfers,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfers,
)
from .treasury_financial_accounts_feature_create_body_intra_stripe_flows import (
    TreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows,
)
from .treasury_financial_accounts_feature_create_body_outbound_payments import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundPayments,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPayments,
)
from .treasury_financial_accounts_feature_create_body_outbound_transfers import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers,
)


class TreasuryFinancialAccountsFeatureCreateBody(
    typing_extensions.TypedDict, total=False
):
    """
    TreasuryFinancialAccountsFeatureCreateBody
    """

    card_issuing: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyCardIssuing
    ]
    """
    Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
    """

    deposit_insurance: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyDepositInsurance
    ]
    """
    Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_addresses: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses
    ]
    """
    Contains Features that add FinancialAddresses to the FinancialAccount.
    """

    inbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyInboundTransfers
    ]
    """
    Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
    """

    intra_stripe_flows: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows
    ]
    """
    Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
    """

    outbound_payments: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundPayments
    ]
    """
    Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
    """

    outbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers
    ]
    """
    Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
    """


class _SerializerTreasuryFinancialAccountsFeatureCreateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    card_issuing: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    deposit_insurance: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyDepositInsurance
    ] = pydantic.Field(alias="deposit_insurance", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    financial_addresses: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses
    ] = pydantic.Field(alias="financial_addresses", default=None)
    inbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfers
    ] = pydantic.Field(alias="inbound_transfers", default=None)
    intra_stripe_flows: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows
    ] = pydantic.Field(alias="intra_stripe_flows", default=None)
    outbound_payments: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPayments
    ] = pydantic.Field(alias="outbound_payments", default=None)
    outbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers
    ] = pydantic.Field(alias="outbound_transfers", default=None)
