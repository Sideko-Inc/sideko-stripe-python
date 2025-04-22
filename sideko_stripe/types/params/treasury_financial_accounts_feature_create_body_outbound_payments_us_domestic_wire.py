import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsUsDomesticWire handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
