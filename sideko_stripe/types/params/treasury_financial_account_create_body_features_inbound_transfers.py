import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features_inbound_transfers_ach import (
    TreasuryFinancialAccountCreateBodyFeaturesInboundTransfersAch,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesInboundTransfersAch,
)


class TreasuryFinancialAccountCreateBodyFeaturesInboundTransfers(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesInboundTransfers
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesInboundTransfersAch
    ]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesInboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesInboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesInboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
