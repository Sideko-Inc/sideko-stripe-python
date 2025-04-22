import pydantic
import typing


class LegalEntityJapanAddress(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City/Ward.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: typing.Optional[str] = pydantic.Field(alias="line1", default=None)
    """
    Block/Building number.
    """
    line2: typing.Optional[str] = pydantic.Field(alias="line2", default=None)
    """
    Building details.
    """
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    """
    ZIP or postal code.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    Prefecture.
    """
    town: typing.Optional[str] = pydantic.Field(alias="town", default=None)
    """
    Town/cho-me.
    """
