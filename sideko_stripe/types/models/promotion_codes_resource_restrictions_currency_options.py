import pydantic
import typing

from .promotion_code_currency_option import PromotionCodeCurrencyOption


class PromotionCodesResourceRestrictionsCurrencyOptions(pydantic.BaseModel):
    """
    Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, PromotionCodeCurrencyOption]
