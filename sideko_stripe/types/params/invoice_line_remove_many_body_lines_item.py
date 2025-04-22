import pydantic
import typing_extensions


class InvoiceLineRemoveManyBodyLinesItem(typing_extensions.TypedDict):
    """
    InvoiceLineRemoveManyBodyLinesItem
    """

    behavior: typing_extensions.Required[
        typing_extensions.Literal["delete", "unassign"]
    ]

    id: typing_extensions.Required[str]


class _SerializerInvoiceLineRemoveManyBodyLinesItem(pydantic.BaseModel):
    """
    Serializer for InvoiceLineRemoveManyBodyLinesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    behavior: typing_extensions.Literal["delete", "unassign"] = pydantic.Field(
        alias="behavior",
    )
    id: str = pydantic.Field(
        alias="id",
    )
