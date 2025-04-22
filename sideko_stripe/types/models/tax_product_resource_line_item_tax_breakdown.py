import pydantic
import typing
import typing_extensions

from .tax_product_resource_jurisdiction import TaxProductResourceJurisdiction
from .tax_product_resource_line_item_tax_rate_details import (
    TaxProductResourceLineItemTaxRateDetails,
)


class TaxProductResourceLineItemTaxBreakdown(pydantic.BaseModel):
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
    jurisdiction: TaxProductResourceJurisdiction = pydantic.Field(
        alias="jurisdiction",
    )
    sourcing: typing_extensions.Literal["destination", "origin"] = pydantic.Field(
        alias="sourcing",
    )
    """
    Indicates whether the jurisdiction was determined by the origin (merchant's address) or destination (customer's address).
    """
    tax_rate_details: typing.Optional[TaxProductResourceLineItemTaxRateDetails] = (
        pydantic.Field(alias="tax_rate_details", default=None)
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
    The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
    """
    taxable_amount: int = pydantic.Field(
        alias="taxable_amount",
    )
    """
    The amount on which tax is calculated, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
