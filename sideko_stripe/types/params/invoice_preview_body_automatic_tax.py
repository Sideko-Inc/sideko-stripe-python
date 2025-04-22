import pydantic
import typing
import typing_extensions

from .invoice_preview_body_automatic_tax_liability import (
    InvoicePreviewBodyAutomaticTaxLiability,
    _SerializerInvoicePreviewBodyAutomaticTaxLiability,
)


class InvoicePreviewBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this invoice preview.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[InvoicePreviewBodyAutomaticTaxLiability]


class _SerializerInvoicePreviewBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[_SerializerInvoicePreviewBodyAutomaticTaxLiability] = (
        pydantic.Field(alias="liability", default=None)
    )
