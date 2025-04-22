import pydantic
import typing
import typing_extensions

from .payment_link_update_body_line_items_item_adjustable_quantity import (
    PaymentLinkUpdateBodyLineItemsItemAdjustableQuantity,
    _SerializerPaymentLinkUpdateBodyLineItemsItemAdjustableQuantity,
)


class PaymentLinkUpdateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyLineItemsItem
    """

    adjustable_quantity: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyLineItemsItemAdjustableQuantity
    ]

    id: typing_extensions.Required[str]

    quantity: typing_extensions.NotRequired[int]


class _SerializerPaymentLinkUpdateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        _SerializerPaymentLinkUpdateBodyLineItemsItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    id: str = pydantic.Field(
        alias="id",
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
