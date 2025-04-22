import pydantic
import typing
import typing_extensions


class TaxProductResourceTaxSettingsDefaults(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "inferred_by_currency"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    """
    Default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) used to specify whether the price is considered inclusive of taxes or exclusive of taxes. If the item's price has a tax behavior set, it will take precedence over the default tax behavior.
    """
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    """
    Default [tax code](https://stripe.com/docs/tax/tax-categories) used to classify your products and prices.
    """
