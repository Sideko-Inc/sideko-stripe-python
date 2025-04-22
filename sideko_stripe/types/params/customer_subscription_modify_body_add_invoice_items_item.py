import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_add_invoice_items_item_discounts_item import (
    CustomerSubscriptionModifyBodyAddInvoiceItemsItemDiscountsItem,
    _SerializerCustomerSubscriptionModifyBodyAddInvoiceItemsItemDiscountsItem,
)
from .customer_subscription_modify_body_add_invoice_items_item_price_data import (
    CustomerSubscriptionModifyBodyAddInvoiceItemsItemPriceData,
    _SerializerCustomerSubscriptionModifyBodyAddInvoiceItemsItemPriceData,
)


class CustomerSubscriptionModifyBodyAddInvoiceItemsItem(typing_extensions.TypedDict):
    """
    CustomerSubscriptionModifyBodyAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[CustomerSubscriptionModifyBodyAddInvoiceItemsItemDiscountsItem]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerCustomerSubscriptionModifyBodyAddInvoiceItemsItem(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[
            _SerializerCustomerSubscriptionModifyBodyAddInvoiceItemsItemDiscountsItem
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
