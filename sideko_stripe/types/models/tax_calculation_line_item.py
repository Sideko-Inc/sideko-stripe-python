import pydantic
import typing
import typing_extensions

from .tax_product_resource_line_item_tax_breakdown import (
    TaxProductResourceLineItemTaxBreakdown,
)


class TaxCalculationLineItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The line item amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    The amount of tax calculated for this line item, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["tax.calculation_line_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    """
    The ID of an existing [Product](https://stripe.com/docs/api/products/object).
    """
    quantity: int = pydantic.Field(
        alias="quantity",
    )
    """
    The number of units of the item being purchased. For reversals, this is the quantity reversed.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    A custom identifier for this line item.
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
    Detailed account of taxes relevant to this line item.
    """
    tax_code: str = pydantic.Field(
        alias="tax_code",
    )
    """
    The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for this resource.
    """
