import pydantic
import typing
import typing_extensions

from .tax_rate import TaxRate


class LineItemsTaxAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount of tax applied for this rate.
    """
    rate: TaxRate = pydantic.Field(
        alias="rate",
    )
    """
    Tax rates can be applied to [invoices](/invoicing/taxes/tax-rates), [subscriptions](/billing/taxes/tax-rates) and [Checkout Sessions](/payments/checkout/use-manual-tax-rates) to collect tax.
    
    Related guide: [Tax rates](/billing/taxes/tax-rates)
    """
    taxability_reason: typing.Optional[
        typing_extensions.Literal[
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
        ]
    ] = pydantic.Field(alias="taxability_reason", default=None)
    """
    The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
    """
    taxable_amount: typing.Optional[int] = pydantic.Field(
        alias="taxable_amount", default=None
    )
    """
    The amount on which tax is calculated, in cents (or local equivalent).
    """
