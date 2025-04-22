import pydantic
import typing
import typing_extensions


class QuoteUpdateBodyLineItemsItemPriceDataRecurring(typing_extensions.TypedDict):
    """
    QuoteUpdateBodyLineItemsItemPriceDataRecurring
    """

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]


class _SerializerQuoteUpdateBodyLineItemsItemPriceDataRecurring(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyLineItemsItemPriceDataRecurring handling case conversions
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
