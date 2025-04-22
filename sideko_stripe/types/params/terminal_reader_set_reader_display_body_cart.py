import pydantic
import typing
import typing_extensions

from .terminal_reader_set_reader_display_body_cart_line_items_item import (
    TerminalReaderSetReaderDisplayBodyCartLineItemsItem,
    _SerializerTerminalReaderSetReaderDisplayBodyCartLineItemsItem,
)


class TerminalReaderSetReaderDisplayBodyCart(typing_extensions.TypedDict):
    """
    Cart
    """

    currency: typing_extensions.Required[str]

    line_items: typing_extensions.Required[
        typing.List[TerminalReaderSetReaderDisplayBodyCartLineItemsItem]
    ]

    tax: typing_extensions.NotRequired[int]

    total: typing_extensions.Required[int]


class _SerializerTerminalReaderSetReaderDisplayBodyCart(pydantic.BaseModel):
    """
    Serializer for TerminalReaderSetReaderDisplayBodyCart handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    line_items: typing.List[
        _SerializerTerminalReaderSetReaderDisplayBodyCartLineItemsItem
    ] = pydantic.Field(
        alias="line_items",
    )
    tax: typing.Optional[int] = pydantic.Field(alias="tax", default=None)
    total: int = pydantic.Field(
        alias="total",
    )
