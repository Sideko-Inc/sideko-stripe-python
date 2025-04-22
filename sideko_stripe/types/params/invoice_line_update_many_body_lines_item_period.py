import pydantic
import typing_extensions


class InvoiceLineUpdateManyBodyLinesItemPeriod(typing_extensions.TypedDict):
    """
    InvoiceLineUpdateManyBodyLinesItemPeriod
    """

    end: typing_extensions.Required[int]

    start: typing_extensions.Required[int]


class _SerializerInvoiceLineUpdateManyBodyLinesItemPeriod(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItemPeriod handling case conversions
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
