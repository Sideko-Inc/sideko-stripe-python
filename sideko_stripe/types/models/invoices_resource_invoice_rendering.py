import pydantic
import typing

from .invoice_rendering_pdf import InvoiceRenderingPdf


class InvoicesResourceInvoiceRendering(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[str] = pydantic.Field(
        alias="amount_tax_display", default=None
    )
    """
    How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
    """
    pdf: typing.Optional[InvoiceRenderingPdf] = pydantic.Field(
        alias="pdf", default=None
    )
    template: typing.Optional[str] = pydantic.Field(alias="template", default=None)
    """
    ID of the rendering template that the invoice is formatted by.
    """
    template_version: typing.Optional[int] = pydantic.Field(
        alias="template_version", default=None
    )
    """
    Version of the rendering template that the invoice is using.
    """
