import pydantic
import typing
import typing_extensions


class PriceListRecurring(typing_extensions.TypedDict):
    """
    Only return prices with these recurring fields.
    """

    interval: typing_extensions.NotRequired[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    meter: typing_extensions.NotRequired[str]

    usage_type: typing_extensions.NotRequired[
        typing_extensions.Literal["licensed", "metered"]
    ]


class _SerializerPriceListRecurring(pydantic.BaseModel):
    """
    Serializer for PriceListRecurring handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    interval: typing.Optional[
        typing_extensions.Literal["day", "month", "week", "year"]
    ] = pydantic.Field(alias="interval", default=None)
    meter: typing.Optional[str] = pydantic.Field(alias="meter", default=None)
    usage_type: typing.Optional[typing_extensions.Literal["licensed", "metered"]] = (
        pydantic.Field(alias="usage_type", default=None)
    )
