import pydantic
import typing
import typing_extensions

from .tax_product_resource_line_item_tax_breakdown import (
    TaxProductResourceLineItemTaxBreakdown,
)


class TaxProductResourceTaxCalculationShippingCost(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The shipping amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    The amount of tax calculated for shipping, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    """
    The ID of an existing [ShippingRate](https://stripe.com/docs/api/shipping_rates/object).
    """
    tax_behavior: typing_extensions.Literal["exclusive", "inclusive"] = pydantic.Field(
        alias="tax_behavior",
    )
    """
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
    """
    tax_breakdown: typing.Optional[
        typing.List[TaxProductResourceLineItemTaxBreakdown]
    ] = pydantic.Field(alias="tax_breakdown", default=None)
    """
    Detailed account of taxes relevant to shipping cost.
    """
    tax_code: str = pydantic.Field(
        alias="tax_code",
    )
    """
    The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for shipping.
    """
