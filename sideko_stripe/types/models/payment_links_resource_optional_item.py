import pydantic
import typing

from .payment_links_resource_optional_item_adjustable_quantity import (
    PaymentLinksResourceOptionalItemAdjustableQuantity,
)


class PaymentLinksResourceOptionalItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adjustable_quantity: typing.Optional[
        PaymentLinksResourceOptionalItemAdjustableQuantity
    ] = pydantic.Field(alias="adjustable_quantity", default=None)
    price: str = pydantic.Field(
        alias="price",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
