import pydantic
import typing
import typing_extensions

from .quote_update_body_line_items_item_discounts_arr0_item import (
    QuoteUpdateBodyLineItemsItemDiscountsArr0Item,
    _SerializerQuoteUpdateBodyLineItemsItemDiscountsArr0Item,
)
from .quote_update_body_line_items_item_price_data import (
    QuoteUpdateBodyLineItemsItemPriceData,
    _SerializerQuoteUpdateBodyLineItemsItemPriceData,
)


class QuoteUpdateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    QuoteUpdateBodyLineItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[QuoteUpdateBodyLineItemsItemDiscountsArr0Item], str]
    ]

    id: typing_extensions.NotRequired[str]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[QuoteUpdateBodyLineItemsItemPriceData]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerQuoteUpdateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerQuoteUpdateBodyLineItemsItemDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[_SerializerQuoteUpdateBodyLineItemsItemPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
