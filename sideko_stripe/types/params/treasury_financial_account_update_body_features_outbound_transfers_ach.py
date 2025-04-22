import pydantic
import typing_extensions


class TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
