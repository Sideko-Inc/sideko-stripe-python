import pydantic
import typing


class SourceOrderItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The amount (price) for this order item.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    This currency of this order item. Required when `amount` is present.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Human-readable description for this order item.
    """
    parent: typing.Optional[str] = pydantic.Field(alias="parent", default=None)
    """
    The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU).
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.
    """
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    The type of this order item. Must be `sku`, `tax`, or `shipping`.
    """
