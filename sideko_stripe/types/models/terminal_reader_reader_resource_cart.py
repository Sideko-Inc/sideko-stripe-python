import pydantic
import typing

from .terminal_reader_reader_resource_line_item import (
    TerminalReaderReaderResourceLineItem,
)


class TerminalReaderReaderResourceCart(pydantic.BaseModel):
    """
    Represents a cart to be displayed on the reader
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    line_items: typing.List[TerminalReaderReaderResourceLineItem] = pydantic.Field(
        alias="line_items",
    )
    """
    List of line items in the cart.
    """
    tax: typing.Optional[int] = pydantic.Field(alias="tax", default=None)
    """
    Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    total: int = pydantic.Field(
        alias="total",
    )
    """
    Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
