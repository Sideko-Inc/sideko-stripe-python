import pydantic
import typing_extensions


class InvoiceLineCreateManyBodyLinesItemPeriod(typing_extensions.TypedDict):
    """
    InvoiceLineCreateManyBodyLinesItemPeriod
    """

    end: typing_extensions.Required[int]

    start: typing_extensions.Required[int]


class _SerializerInvoiceLineCreateManyBodyLinesItemPeriod(pydantic.BaseModel):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItemPeriod handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end: int = pydantic.Field(
        alias="end",
    )
    start: int = pydantic.Field(
        alias="start",
    )
