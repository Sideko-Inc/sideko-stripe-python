import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_feature_create_body_outbound_transfers_ach import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersAch,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersAch,
)
from .treasury_financial_accounts_feature_create_body_outbound_transfers_us_domestic_wire import (
    TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersUsDomesticWire,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersUsDomesticWire,
)


class TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers(
    typing_extensions.TypedDict
):
    """
    Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersAch
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersUsDomesticWire
    ]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyOutboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
    us_domestic_wire: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundTransfersUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
