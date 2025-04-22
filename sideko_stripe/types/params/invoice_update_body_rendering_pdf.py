import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyRenderingPdf(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyRenderingPdf
    """

    page_size: typing_extensions.NotRequired[
        typing_extensions.Literal["a4", "auto", "letter"]
    ]


class _SerializerInvoiceUpdateBodyRenderingPdf(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyRenderingPdf handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    page_size: typing.Optional[typing_extensions.Literal["a4", "auto", "letter"]] = (
        pydantic.Field(alias="page_size", default=None)
    )
