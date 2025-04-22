import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features_outbound_transfers_ach import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch,
)
from .treasury_financial_account_update_body_features_outbound_transfers_us_domestic_wire import (
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire,
)


class TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
