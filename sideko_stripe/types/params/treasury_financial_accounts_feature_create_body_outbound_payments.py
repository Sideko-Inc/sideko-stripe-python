import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_feature_create_body_outbound_payments_ach import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch,
)
from .treasury_financial_accounts_feature_create_body_outbound_payments_us_domestic_wire import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire,
)


class TreasuryFinancialAccountsFeatureCreateBodyOutboundPayments(
    typing_extensions.TypedDict
):
    """
    Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPayments(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyOutboundPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
