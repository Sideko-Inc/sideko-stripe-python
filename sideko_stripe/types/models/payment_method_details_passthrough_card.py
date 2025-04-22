import pydantic
import typing


class PaymentMethodDetailsPassthroughCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    """
    Two-digit number representing the card's expiration month.
    """
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    """
    Four-digit number representing the card's expiration year.
    """
    funding: typing.Optional[str] = pydantic.Field(alias="funding", default=None)
    """
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the card.
    """
