import pydantic
import typing
import typing_extensions

from .payment_link_create_body_line_items_item_adjustable_quantity import (
    PaymentLinkCreateBodyLineItemsItemAdjustableQuantity,
    _SerializerPaymentLinkCreateBodyLineItemsItemAdjustableQuantity,
)


class PaymentLinkCreateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyLineItemsItem
    """

    adjustable_quantity: typing_extensions.NotRequired[
        PaymentLinkCreateBodyLineItemsItemAdjustableQuantity
    ]

    price: typing_extensions.Required[str]

    quantity: typing_extensions.Required[int]


class _SerializerPaymentLinkCreateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        _SerializerPaymentLinkCreateBodyLineItemsItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    price: str = pydantic.Field(
        alias="price",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
