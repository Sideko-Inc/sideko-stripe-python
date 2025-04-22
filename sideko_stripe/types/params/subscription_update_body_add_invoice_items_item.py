import pydantic
import typing
import typing_extensions

from .subscription_update_body_add_invoice_items_item_discounts_item import (
    SubscriptionUpdateBodyAddInvoiceItemsItemDiscountsItem,
    _SerializerSubscriptionUpdateBodyAddInvoiceItemsItemDiscountsItem,
)
from .subscription_update_body_add_invoice_items_item_price_data import (
    SubscriptionUpdateBodyAddInvoiceItemsItemPriceData,
    _SerializerSubscriptionUpdateBodyAddInvoiceItemsItemPriceData,
)


class SubscriptionUpdateBodyAddInvoiceItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionUpdateBodyAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[SubscriptionUpdateBodyAddInvoiceItemsItemDiscountsItem]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionUpdateBodyAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionUpdateBodyAddInvoiceItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBodyAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[_SerializerSubscriptionUpdateBodyAddInvoiceItemsItemDiscountsItem]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionUpdateBodyAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
