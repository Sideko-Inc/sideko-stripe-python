import pydantic
import typing
import typing_extensions

from .climate_removals_location import ClimateRemovalsLocation


class ClimateSupplier(pydantic.BaseModel):
    """
    A supplier of carbon removal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    info_url: str = pydantic.Field(
        alias="info_url",
    )
    """
    Link to a webpage to learn more about the supplier.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    locations: typing.List[ClimateRemovalsLocation] = pydantic.Field(
        alias="locations",
    )
    """
    The locations in which this supplier operates.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Name of this carbon removal supplier.
    """
    object: typing_extensions.Literal["climate.supplier"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object’s type. Objects of the same type share the same value.
    """
    removal_pathway: typing_extensions.Literal[
        "biomass_carbon_removal_and_storage",
        "direct_air_capture",
        "enhanced_weathering",
    ] = pydantic.Field(
        alias="removal_pathway",
    )
    """
    The scientific pathway used for carbon removal.
    """
