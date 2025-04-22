import pydantic
import typing_extensions


class TerminalReaderSetReaderDisplayBodyCartLineItemsItem(typing_extensions.TypedDict):
    """
    TerminalReaderSetReaderDisplayBodyCartLineItemsItem
    """

    amount: typing_extensions.Required[int]

    description: typing_extensions.Required[str]

    quantity: typing_extensions.Required[int]


class _SerializerTerminalReaderSetReaderDisplayBodyCartLineItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for TerminalReaderSetReaderDisplayBodyCartLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    description: str = pydantic.Field(
        alias="description",
    )
    quantity: int = pydantic.Field(
        alias="quantity",
    )
