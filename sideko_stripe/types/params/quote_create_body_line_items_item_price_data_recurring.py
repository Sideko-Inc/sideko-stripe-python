import pydantic
import typing
import typing_extensions


class QuoteCreateBodyLineItemsItemPriceDataRecurring(typing_extensions.TypedDict):
    """
    QuoteCreateBodyLineItemsItemPriceDataRecurring
    """

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]


class _SerializerQuoteCreateBodyLineItemsItemPriceDataRecurring(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyLineItemsItemPriceDataRecurring handling case conversions
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
