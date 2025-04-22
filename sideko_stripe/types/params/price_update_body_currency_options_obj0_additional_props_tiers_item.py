import pydantic
import typing
import typing_extensions


class PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem(
    typing_extensions.TypedDict
):
    """
    PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem
    """

    flat_amount: typing_extensions.NotRequired[int]

    flat_amount_decimal: typing_extensions.NotRequired[str]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]

    up_to: typing_extensions.Required[
        typing.Union[typing_extensions.Literal["inf"], int]
    ]


class _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem(
    pydantic.BaseModel
):
    """
    Serializer for PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    flat_amount: typing.Optional[int] = pydantic.Field(
        alias="flat_amount", default=None
    )
    flat_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="flat_amount_decimal", default=None
    )
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
    up_to: typing.Union[typing_extensions.Literal["inf"], int] = pydantic.Field(
        alias="up_to",
    )
