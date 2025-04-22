import pydantic
import typing
import typing_extensions

from .invoice_create_body_rendering_pdf import (
    InvoiceCreateBodyRenderingPdf,
    _SerializerInvoiceCreateBodyRenderingPdf,
)


class InvoiceCreateBodyRendering(typing_extensions.TypedDict):
    """
    The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    """

    amount_tax_display: typing_extensions.NotRequired[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ]

    pdf: typing_extensions.NotRequired[InvoiceCreateBodyRenderingPdf]

    template: typing_extensions.NotRequired[str]

    template_version: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerInvoiceCreateBodyRendering(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyRendering handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ] = pydantic.Field(alias="amount_tax_display", default=None)
    pdf: typing.Optional[_SerializerInvoiceCreateBodyRenderingPdf] = pydantic.Field(
        alias="pdf", default=None
    )
    template: typing.Optional[str] = pydantic.Field(alias="template", default=None)
    template_version: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="template_version", default=None
    )
