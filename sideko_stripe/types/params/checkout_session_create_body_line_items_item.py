import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_line_items_item_adjustable_quantity import (
    CheckoutSessionCreateBodyLineItemsItemAdjustableQuantity,
    _SerializerCheckoutSessionCreateBodyLineItemsItemAdjustableQuantity,
)
from .checkout_session_create_body_line_items_item_price_data import (
    CheckoutSessionCreateBodyLineItemsItemPriceData,
    _SerializerCheckoutSessionCreateBodyLineItemsItemPriceData,
)


class CheckoutSessionCreateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyLineItemsItem
    """

    adjustable_quantity: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyLineItemsItemAdjustableQuantity
    ]

    dynamic_tax_rates: typing_extensions.NotRequired[typing.List[str]]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyLineItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.List[str]]


class _SerializerCheckoutSessionCreateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        _SerializerCheckoutSessionCreateBodyLineItemsItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    dynamic_tax_rates: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="dynamic_tax_rates", default=None
    )
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyLineItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
