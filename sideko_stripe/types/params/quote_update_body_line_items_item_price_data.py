import pydantic
import typing
import typing_extensions

from .quote_update_body_line_items_item_price_data_recurring import (
    QuoteUpdateBodyLineItemsItemPriceDataRecurring,
    _SerializerQuoteUpdateBodyLineItemsItemPriceDataRecurring,
)


class QuoteUpdateBodyLineItemsItemPriceData(typing_extensions.TypedDict):
    """
    QuoteUpdateBodyLineItemsItemPriceData
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.Required[str]

    recurring: typing_extensions.NotRequired[
        QuoteUpdateBodyLineItemsItemPriceDataRecurring
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerQuoteUpdateBodyLineItemsItemPriceData(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyLineItemsItemPriceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    product: str = pydantic.Field(
        alias="product",
    )
    recurring: typing.Optional[
        _SerializerQuoteUpdateBodyLineItemsItemPriceDataRecurring
    ] = pydantic.Field(alias="recurring", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
