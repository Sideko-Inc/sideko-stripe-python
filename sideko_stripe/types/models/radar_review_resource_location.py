import pydantic
import typing


class RadarReviewResourceLocation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    The city where the payment originated.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country where the payment originated.
    """
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    """
    The geographic latitude where the payment originated.
    """
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    """
    The geographic longitude where the payment originated.
    """
    region: typing.Optional[str] = pydantic.Field(alias="region", default=None)
    """
    The state/county/province/region where the payment originated.
    """
