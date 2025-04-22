import pydantic
import typing_extensions


class TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesOutboundPaymentsUsDomesticWire handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
