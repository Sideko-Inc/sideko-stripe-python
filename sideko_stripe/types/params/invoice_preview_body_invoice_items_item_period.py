import pydantic
import typing_extensions


class InvoicePreviewBodyInvoiceItemsItemPeriod(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyInvoiceItemsItemPeriod
    """

    end: typing_extensions.Required[int]

    start: typing_extensions.Required[int]


class _SerializerInvoicePreviewBodyInvoiceItemsItemPeriod(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyInvoiceItemsItemPeriod handling case conversions
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
