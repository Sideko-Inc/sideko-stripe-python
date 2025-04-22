import pydantic
import typing


class ClimateRemovalsLocation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    The city where the supplier is located.
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter ISO code representing the country where the supplier is located.
    """
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    """
    The geographic latitude where the supplier is located.
    """
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    """
    The geographic longitude where the supplier is located.
    """
    region: typing.Optional[str] = pydantic.Field(alias="region", default=None)
    """
    The state/county/province/region where the supplier is located.
    """
