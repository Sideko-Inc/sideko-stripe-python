import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_optional_items_item_adjustable_quantity import (
    CheckoutSessionCreateBodyOptionalItemsItemAdjustableQuantity,
    _SerializerCheckoutSessionCreateBodyOptionalItemsItemAdjustableQuantity,
)


class CheckoutSessionCreateBodyOptionalItemsItem(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyOptionalItemsItem
    """

    adjustable_quantity: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyOptionalItemsItemAdjustableQuantity
    ]

    price: typing_extensions.Required[str]

    quantity: typing_extensions.Required[int]


class _SerializerCheckoutSessionCreateBodyOptionalItemsItem(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyOptionalItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        _SerializerCheckoutSessionCreateBodyOptionalItemsItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    price: str = pydantic.Field(
        alias="price",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
