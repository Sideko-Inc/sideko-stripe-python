import pydantic
import typing
import typing_extensions


class PriceCreateBodyRecurring(typing_extensions.TypedDict):
    """
    The recurring components of a price such as `interval` and `usage_type`.
    """

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]

    meter: typing_extensions.NotRequired[str]

    usage_type: typing_extensions.NotRequired[
        typing_extensions.Literal["licensed", "metered"]
    ]


class _SerializerPriceCreateBodyRecurring(pydantic.BaseModel):
    """
    Serializer for PriceCreateBodyRecurring handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    interval: typing_extensions.Literal["day", "month", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    meter: typing.Optional[str] = pydantic.Field(alias="meter", default=None)
    usage_type: typing.Optional[typing_extensions.Literal["licensed", "metered"]] = (
        pydantic.Field(alias="usage_type", default=None)
    )
