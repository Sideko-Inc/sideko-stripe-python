import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_taxes_tax_rate_details import (
    BillingBillResourceInvoicingTaxesTaxRateDetails,
)


class BillingBillResourceInvoicingTaxesTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of the tax, in cents (or local equivalent).
    """
    tax_behavior: typing_extensions.Literal["exclusive", "inclusive"] = pydantic.Field(
        alias="tax_behavior",
    )
    """
    Whether this tax is inclusive or exclusive.
    """
    tax_rate_details: typing.Optional[
        BillingBillResourceInvoicingTaxesTaxRateDetails
    ] = pydantic.Field(alias="tax_rate_details", default=None)
    taxability_reason: typing_extensions.Literal[
        "customer_exempt",
        "not_available",
        "not_collecting",
        "not_subject_to_tax",
        "not_supported",
        "portion_product_exempt",
        "portion_reduced_rated",
        "portion_standard_rated",
        "product_exempt",
        "product_exempt_holiday",
        "proportionally_rated",
        "reduced_rated",
        "reverse_charge",
        "standard_rated",
        "taxable_basis_reduced",
        "zero_rated",
    ] = pydantic.Field(
        alias="taxability_reason",
    )
    """
    The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
    """
    taxable_amount: typing.Optional[int] = pydantic.Field(
        alias="taxable_amount", default=None
    )
    """
    The amount on which tax is calculated, in cents (or local equivalent).
    """
    type_: typing_extensions.Literal["tax_rate_details"] = pydantic.Field(
        alias="type",
    )
    """
    The type of tax information.
    """
