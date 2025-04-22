import pydantic
import typing


class AccountAnnualRevenue(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    A non-negative integer representing the amount in the [smallest currency unit](/currencies#zero-decimal).
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    fiscal_year_end: typing.Optional[str] = pydantic.Field(
        alias="fiscal_year_end", default=None
    )
    """
    The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
    """
