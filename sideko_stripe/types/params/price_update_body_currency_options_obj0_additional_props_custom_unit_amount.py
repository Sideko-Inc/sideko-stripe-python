import pydantic
import typing
import typing_extensions


class PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount(
    typing_extensions.TypedDict
):
    """
    PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount
    """

    enabled: typing_extensions.Required[bool]

    maximum: typing_extensions.NotRequired[int]

    minimum: typing_extensions.NotRequired[int]

    preset: typing_extensions.NotRequired[int]


class _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount(
    pydantic.BaseModel
):
    """
    Serializer for PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    maximum: typing.Optional[int] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[int] = pydantic.Field(alias="minimum", default=None)
    preset: typing.Optional[int] = pydantic.Field(alias="preset", default=None)
