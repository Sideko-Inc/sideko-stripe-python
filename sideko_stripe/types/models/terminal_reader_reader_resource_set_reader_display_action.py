import pydantic
import typing
import typing_extensions

from .terminal_reader_reader_resource_cart import TerminalReaderReaderResourceCart


class TerminalReaderReaderResourceSetReaderDisplayAction(pydantic.BaseModel):
    """
    Represents a reader action to set the reader display
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cart: typing.Optional[TerminalReaderReaderResourceCart] = pydantic.Field(
        alias="cart", default=None
    )
    """
    Represents a cart to be displayed on the reader
    """
    type_: typing_extensions.Literal["cart"] = pydantic.Field(
        alias="type",
    )
    """
    Type of information to be displayed by the reader.
    """
