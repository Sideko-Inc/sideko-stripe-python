import pydantic
import typing_extensions

from .tax_product_resource_tax_rate_details import TaxProductResourceTaxRateDetails


class TaxProductResourceTaxBreakdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of tax, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    inclusive: bool = pydantic.Field(
        alias="inclusive",
    )
    """
    Specifies whether the tax amount is included in the line item amount.
    """
    tax_rate_details: TaxProductResourceTaxRateDetails = pydantic.Field(
        alias="tax_rate_details",
    )
    taxability_reason: typing_extensions.Literal[
        "customer_exempt",
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
    The reasoning behind this tax, for example, if the product is tax exempt. We might extend the possible values for this field to support new tax rules.
    """
    taxable_amount: int = pydantic.Field(
        alias="taxable_amount",
    )
    """
    The amount on which tax is calculated, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
