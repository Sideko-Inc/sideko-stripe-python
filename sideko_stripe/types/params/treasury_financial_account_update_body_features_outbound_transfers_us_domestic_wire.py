import pydantic
import typing_extensions


class TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesOutboundTransfersUsDomesticWire handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
