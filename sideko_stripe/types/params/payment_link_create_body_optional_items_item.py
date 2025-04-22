import pydantic
import typing
import typing_extensions

from .payment_link_create_body_optional_items_item_adjustable_quantity import (
    PaymentLinkCreateBodyOptionalItemsItemAdjustableQuantity,
    _SerializerPaymentLinkCreateBodyOptionalItemsItemAdjustableQuantity,
)


class PaymentLinkCreateBodyOptionalItemsItem(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyOptionalItemsItem
    """

    adjustable_quantity: typing_extensions.NotRequired[
        PaymentLinkCreateBodyOptionalItemsItemAdjustableQuantity
    ]

    price: typing_extensions.Required[str]

    quantity: typing_extensions.Required[int]


class _SerializerPaymentLinkCreateBodyOptionalItemsItem(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyOptionalItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        _SerializerPaymentLinkCreateBodyOptionalItemsItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    price: str = pydantic.Field(
        alias="price",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
