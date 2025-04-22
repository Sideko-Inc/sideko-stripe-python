import pydantic
import typing_extensions


class TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesOutboundTransfersAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
