import pydantic
import typing

from .climate_removals_location import ClimateRemovalsLocation
from .climate_supplier import ClimateSupplier


class ClimateRemovalsOrderDeliveries(pydantic.BaseModel):
    """
    The delivery of a specified quantity of carbon for an order.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    delivered_at: int = pydantic.Field(
        alias="delivered_at",
    )
    """
    Time at which the delivery occurred. Measured in seconds since the Unix epoch.
    """
    location: typing.Optional[ClimateRemovalsLocation] = pydantic.Field(
        alias="location", default=None
    )
    metric_tons: str = pydantic.Field(
        alias="metric_tons",
    )
    """
    Quantity of carbon removal supplied by this delivery.
    """
    registry_url: typing.Optional[str] = pydantic.Field(
        alias="registry_url", default=None
    )
    """
    Once retired, a URL to the registry entry for the tons from this delivery.
    """
    supplier: ClimateSupplier = pydantic.Field(
        alias="supplier",
    )
    """
    A supplier of carbon removal.
    """
