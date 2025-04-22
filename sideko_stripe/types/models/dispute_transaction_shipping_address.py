import pydantic
import typing


class DisputeTransactionShippingAddress(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City, district, suburb, town, or village.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: typing.Optional[str] = pydantic.Field(alias="line1", default=None)
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: typing.Optional[str] = pydantic.Field(alias="line2", default=None)
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    """
    ZIP or postal code.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State, county, province, or region.
    """
