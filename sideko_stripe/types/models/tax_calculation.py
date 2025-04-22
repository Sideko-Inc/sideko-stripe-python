import pydantic
import typing
import typing_extensions

from .tax_calculation_line_items import TaxCalculationLineItems
from .tax_product_resource_customer_details import TaxProductResourceCustomerDetails
from .tax_product_resource_ship_from_details import TaxProductResourceShipFromDetails
from .tax_product_resource_tax_breakdown import TaxProductResourceTaxBreakdown
from .tax_product_resource_tax_calculation_shipping_cost import (
    TaxProductResourceTaxCalculationShippingCost,
)


class TaxCalculation(pydantic.BaseModel):
    """
    A Tax Calculation allows you to calculate the tax to collect from your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total amount after taxes in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    """
    The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource.
    """
    customer_details: TaxProductResourceCustomerDetails = pydantic.Field(
        alias="customer_details",
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    Timestamp of date at which the tax calculation will expire.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the calculation.
    """
    line_items: typing.Optional[TaxCalculationLineItems] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    The list of items the customer is purchasing.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["tax.calculation"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    ship_from_details: typing.Optional[TaxProductResourceShipFromDetails] = (
        pydantic.Field(alias="ship_from_details", default=None)
    )
    shipping_cost: typing.Optional[TaxProductResourceTaxCalculationShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
    tax_amount_exclusive: int = pydantic.Field(
        alias="tax_amount_exclusive",
    )
    """
    The amount of tax to be collected on top of the line item prices.
    """
    tax_amount_inclusive: int = pydantic.Field(
        alias="tax_amount_inclusive",
    )
    """
    The amount of tax already included in the line item prices.
    """
    tax_breakdown: typing.List[TaxProductResourceTaxBreakdown] = pydantic.Field(
        alias="tax_breakdown",
    )
    """
    Breakdown of individual tax amounts that add up to the total.
    """
    tax_date: int = pydantic.Field(
        alias="tax_date",
    )
    """
    Timestamp of date at which the tax rules and rates in effect applies for the calculation.
    """
