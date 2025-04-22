import pydantic
import typing_extensions


class TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesOutboundPaymentsUsDomesticWire handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
