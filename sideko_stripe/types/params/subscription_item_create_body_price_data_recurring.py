import pydantic
import typing
import typing_extensions


class SubscriptionItemCreateBodyPriceDataRecurring(typing_extensions.TypedDict):
    """
    SubscriptionItemCreateBodyPriceDataRecurring
    """

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]


class _SerializerSubscriptionItemCreateBodyPriceDataRecurring(pydantic.BaseModel):
    """
    Serializer for SubscriptionItemCreateBodyPriceDataRecurring handling case conversions
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
