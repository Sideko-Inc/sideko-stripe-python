import pydantic
import typing
import typing_extensions

from .subscription_create_body_add_invoice_items_item_discounts_item import (
    SubscriptionCreateBodyAddInvoiceItemsItemDiscountsItem,
    _SerializerSubscriptionCreateBodyAddInvoiceItemsItemDiscountsItem,
)
from .subscription_create_body_add_invoice_items_item_price_data import (
    SubscriptionCreateBodyAddInvoiceItemsItemPriceData,
    _SerializerSubscriptionCreateBodyAddInvoiceItemsItemPriceData,
)


class SubscriptionCreateBodyAddInvoiceItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionCreateBodyAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[SubscriptionCreateBodyAddInvoiceItemsItemDiscountsItem]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionCreateBodyAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionCreateBodyAddInvoiceItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[_SerializerSubscriptionCreateBodyAddInvoiceItemsItemDiscountsItem]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionCreateBodyAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
