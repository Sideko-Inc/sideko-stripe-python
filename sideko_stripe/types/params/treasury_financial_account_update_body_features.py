import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features_card_issuing import (
    TreasuryFinancialAccountUpdateBodyFeaturesCardIssuing,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesCardIssuing,
)
from .treasury_financial_account_update_body_features_deposit_insurance import (
    TreasuryFinancialAccountUpdateBodyFeaturesDepositInsurance,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesDepositInsurance,
)
from .treasury_financial_account_update_body_features_financial_addresses import (
    TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses,
)
from .treasury_financial_account_update_body_features_inbound_transfers import (
    TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers,
)
from .treasury_financial_account_update_body_features_intra_stripe_flows import (
    TreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows,
)
from .treasury_financial_account_update_body_features_outbound_payments import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments,
)
from .treasury_financial_account_update_body_features_outbound_transfers import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers,
)


class TreasuryFinancialAccountUpdateBodyFeatures(typing_extensions.TypedDict):
    """
    Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field.
    """

    card_issuing: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesCardIssuing
    ]

    deposit_insurance: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesDepositInsurance
    ]

    financial_addresses: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses
    ]

    inbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers
    ]

    intra_stripe_flows: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows
    ]

    outbound_payments: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments
    ]

    outbound_transfers: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyFeatures(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_issuing: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    deposit_insurance: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesDepositInsurance
    ] = pydantic.Field(alias="deposit_insurance", default=None)
    financial_addresses: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses
    ] = pydantic.Field(alias="financial_addresses", default=None)
    inbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers
    ] = pydantic.Field(alias="inbound_transfers", default=None)
    intra_stripe_flows: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows
    ] = pydantic.Field(alias="intra_stripe_flows", default=None)
    outbound_payments: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments
    ] = pydantic.Field(alias="outbound_payments", default=None)
    outbound_transfers: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers
    ] = pydantic.Field(alias="outbound_transfers", default=None)
