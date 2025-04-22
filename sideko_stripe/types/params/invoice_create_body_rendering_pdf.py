import pydantic
import typing
import typing_extensions


class InvoiceCreateBodyRenderingPdf(typing_extensions.TypedDict):
    """
    InvoiceCreateBodyRenderingPdf
    """

    page_size: typing_extensions.NotRequired[
        typing_extensions.Literal["a4", "auto", "letter"]
    ]


class _SerializerInvoiceCreateBodyRenderingPdf(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyRenderingPdf handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    page_size: typing.Optional[typing_extensions.Literal["a4", "auto", "letter"]] = (
        pydantic.Field(alias="page_size", default=None)
    )
