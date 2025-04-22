import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features_outbound_payments_ach import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsAch,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsAch,
)
from .treasury_financial_account_create_body_features_outbound_payments_us_domestic_wire import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire,
)


class TreasuryFinancialAccountCreateBodyFeaturesOutboundPayments(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesOutboundPayments
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPayments(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesOutboundPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
