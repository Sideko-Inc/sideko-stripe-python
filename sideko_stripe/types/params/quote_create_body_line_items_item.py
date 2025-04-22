import pydantic
import typing
import typing_extensions

from .quote_create_body_line_items_item_discounts_arr0_item import (
    QuoteCreateBodyLineItemsItemDiscountsArr0Item,
    _SerializerQuoteCreateBodyLineItemsItemDiscountsArr0Item,
)
from .quote_create_body_line_items_item_price_data import (
    QuoteCreateBodyLineItemsItemPriceData,
    _SerializerQuoteCreateBodyLineItemsItemPriceData,
)


class QuoteCreateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    QuoteCreateBodyLineItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[QuoteCreateBodyLineItemsItemDiscountsArr0Item], str]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[QuoteCreateBodyLineItemsItemPriceData]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerQuoteCreateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerQuoteCreateBodyLineItemsItemDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[_SerializerQuoteCreateBodyLineItemsItemPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
