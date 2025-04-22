import pydantic
import typing
import typing_extensions

from .invoice_update_body_automatic_tax_liability import (
    InvoiceUpdateBodyAutomaticTaxLiability,
    _SerializerInvoiceUpdateBodyAutomaticTaxLiability,
)


class InvoiceUpdateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this invoice.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[InvoiceUpdateBodyAutomaticTaxLiability]


class _SerializerInvoiceUpdateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[_SerializerInvoiceUpdateBodyAutomaticTaxLiability] = (
        pydantic.Field(alias="liability", default=None)
    )
