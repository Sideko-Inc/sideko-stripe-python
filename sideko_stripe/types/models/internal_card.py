import pydantic
import typing


class InternalCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    """
    Brand of the card used in the transaction
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card
    """
    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    """
    Two digit number representing the card's expiration month
    """
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    """
    Two digit number representing the card's expiration year
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last 4 digits of the card
    """
