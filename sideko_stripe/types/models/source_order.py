import pydantic
import typing

from .shipping import Shipping
from .source_order_item import SourceOrderItem


class SourceOrder(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The email address of the customer placing the order.
    """
    items: typing.Optional[typing.List[SourceOrderItem]] = pydantic.Field(
        alias="items", default=None
    )
    """
    List of items constituting the order.
    """
    shipping: typing.Optional[Shipping] = pydantic.Field(alias="shipping", default=None)
