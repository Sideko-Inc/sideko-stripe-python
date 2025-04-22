import pydantic
import typing


class PaymentLinksResourceOptionalItemAdjustableQuantity(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Set to true if the quantity can be adjusted to any non-negative integer.
    """
    maximum: typing.Optional[int] = pydantic.Field(alias="maximum", default=None)
    """
    The maximum quantity of this item the customer can purchase. By default this value is 99.
    """
    minimum: typing.Optional[int] = pydantic.Field(alias="minimum", default=None)
    """
    The minimum quantity of this item the customer must purchase, if they choose to purchase it. Because this item is optional, the customer will always be able to remove it from their order, even if the `minimum` configured here is greater than 0. By default this value is 0.
    """
