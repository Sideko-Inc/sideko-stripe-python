import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features_outbound_transfers_ach import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch,
)
from .treasury_financial_account_create_body_features_outbound_transfers_us_domestic_wire import (
    TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersUsDomesticWire,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersUsDomesticWire,
)


class TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
