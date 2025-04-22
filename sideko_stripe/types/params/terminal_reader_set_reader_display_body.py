import pydantic
import typing
import typing_extensions

from .terminal_reader_set_reader_display_body_cart import (
    TerminalReaderSetReaderDisplayBodyCart,
    _SerializerTerminalReaderSetReaderDisplayBodyCart,
)


class TerminalReaderSetReaderDisplayBody(typing_extensions.TypedDict, total=False):
    """
    TerminalReaderSetReaderDisplayBody
    """

    cart: typing_extensions.NotRequired[TerminalReaderSetReaderDisplayBodyCart]
    """
    Cart
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["cart"]]
    """
    Type
    """


class _SerializerTerminalReaderSetReaderDisplayBody(pydantic.BaseModel):
    """
    Serializer for TerminalReaderSetReaderDisplayBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cart: typing.Optional[_SerializerTerminalReaderSetReaderDisplayBodyCart] = (
        pydantic.Field(alias="cart", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    type_: typing_extensions.Literal["cart"] = pydantic.Field(
        alias="type",
    )
