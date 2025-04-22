import pydantic
import typing
import typing_extensions

from .invoice_create_body_automatic_tax_liability import (
    InvoiceCreateBodyAutomaticTaxLiability,
    _SerializerInvoiceCreateBodyAutomaticTaxLiability,
)


class InvoiceCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this invoice.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[InvoiceCreateBodyAutomaticTaxLiability]


class _SerializerInvoiceCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[_SerializerInvoiceCreateBodyAutomaticTaxLiability] = (
        pydantic.Field(alias="liability", default=None)
    )
