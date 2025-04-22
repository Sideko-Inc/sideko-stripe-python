import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features_inbound_transfers_ach import (
    TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfersAch,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesInboundTransfersAch,
)


class TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfersAch
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesInboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesInboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
