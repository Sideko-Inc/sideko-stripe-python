import pydantic
import typing

from .line_items_tax_amount import LineItemsTaxAmount
from .shipping_rate import ShippingRate


class PaymentPagesCheckoutSessionShippingCost(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total shipping cost before any discounts or taxes are applied.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total shipping cost after discounts and taxes are applied.
    """
    shipping_rate: typing.Optional[typing.Union[str, ShippingRate]] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    """
    The ID of the ShippingRate for this order.
    """
    taxes: typing.Optional[typing.List[LineItemsTaxAmount]] = pydantic.Field(
        alias="taxes", default=None
    )
    """
    The taxes applied to the shipping rate.
    """
