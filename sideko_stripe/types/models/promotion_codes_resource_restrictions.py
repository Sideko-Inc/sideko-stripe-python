import pydantic
import typing

from .promotion_codes_resource_restrictions_currency_options import (
    PromotionCodesResourceRestrictionsCurrencyOptions,
)


class PromotionCodesResourceRestrictions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency_options: typing.Optional[
        PromotionCodesResourceRestrictionsCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
    """
    Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """
    first_time_transaction: bool = pydantic.Field(
        alias="first_time_transaction",
    )
    """
    A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices
    """
    minimum_amount: typing.Optional[int] = pydantic.Field(
        alias="minimum_amount", default=None
    )
    """
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).
    """
    minimum_amount_currency: typing.Optional[str] = pydantic.Field(
        alias="minimum_amount_currency", default=None
    )
    """
    Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount
    """
