import pydantic
import typing

from .payment_pages_checkout_session_optional_item_adjustable_quantity import (
    PaymentPagesCheckoutSessionOptionalItemAdjustableQuantity,
)


class PaymentPagesCheckoutSessionOptionalItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        PaymentPagesCheckoutSessionOptionalItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    price: str = pydantic.Field(
        alias="price",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
