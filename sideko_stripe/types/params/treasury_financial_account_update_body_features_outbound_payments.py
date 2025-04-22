import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features_outbound_payments_ach import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsAch,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsAch,
)
from .treasury_financial_account_update_body_features_outbound_payments_us_domestic_wire import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire,
)


class TreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesOutboundPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
