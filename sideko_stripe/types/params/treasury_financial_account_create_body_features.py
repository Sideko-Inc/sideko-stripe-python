import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features_card_issuing import (
    TreasuryFinancialAccountCreateBodyFeaturesCardIssuing,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesCardIssuing,
)
from .treasury_financial_account_create_body_features_deposit_insurance import (
    TreasuryFinancialAccountCreateBodyFeaturesDepositInsurance,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesDepositInsurance,
)
from .treasury_financial_account_create_body_features_financial_addresses import (
    TreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses,
)
from .treasury_financial_account_create_body_features_inbound_transfers import (
    TreasuryFinancialAccountCreateBodyFeaturesInboundTransfers,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesInboundTransfers,
)
from .treasury_financial_account_create_body_features_intra_stripe_flows import (
    TreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows,
)
from .treasury_financial_account_create_body_features_outbound_payments import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundPayments,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPayments,
)
from .treasury_financial_account_create_body_features_outbound_transfers import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers,
)


class TreasuryFinancialAccountCreateBodyFeatures(typing_extensions.TypedDict):
    """
    Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.
    """

    card_issuing: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesCardIssuing
    ]

    deposit_insurance: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesDepositInsurance
    ]

    financial_addresses: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses
    ]

    inbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesInboundTransfers
    ]

    intra_stripe_flows: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows
    ]

    outbound_payments: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundPayments
    ]

    outbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers
    ]


class _SerializerTreasuryFinancialAccountCreateBodyFeatures(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_issuing: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    deposit_insurance: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesDepositInsurance
    ] = pydantic.Field(alias="deposit_insurance", default=None)
    financial_addresses: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses
    ] = pydantic.Field(alias="financial_addresses", default=None)
    inbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesInboundTransfers
    ] = pydantic.Field(alias="inbound_transfers", default=None)
    intra_stripe_flows: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows
    ] = pydantic.Field(alias="intra_stripe_flows", default=None)
    outbound_payments: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPayments
    ] = pydantic.Field(alias="outbound_payments", default=None)
    outbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers
    ] = pydantic.Field(alias="outbound_transfers", default=None)
