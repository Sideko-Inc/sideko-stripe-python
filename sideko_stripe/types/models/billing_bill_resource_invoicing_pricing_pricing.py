import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_pricing_pricing_price_details import (
    BillingBillResourceInvoicingPricingPricingPriceDetails,
)


class BillingBillResourceInvoicingPricingPricing(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    price_details: typing.Optional[
        BillingBillResourceInvoicingPricingPricingPriceDetails
    ] = pydantic.Field(alias="price_details", default=None)
    type_: typing_extensions.Literal["price_details"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the pricing details.
    """
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
    """
    The unit amount (in the `currency` specified) of the item which contains a decimal value with at most 12 decimal places.
    """
