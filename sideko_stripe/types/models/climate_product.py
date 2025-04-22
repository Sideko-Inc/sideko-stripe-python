import pydantic
import typing
import typing_extensions

from .climate_product_current_prices_per_metric_ton import (
    ClimateProductCurrentPricesPerMetricTon,
)
from .climate_supplier import ClimateSupplier


class ClimateProduct(pydantic.BaseModel):
    """
    A Climate product represents a type of carbon removal unit available for reservation.
    You can retrieve it to see the current price and availability.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    current_prices_per_metric_ton: ClimateProductCurrentPricesPerMetricTon = (
        pydantic.Field(
            alias="current_prices_per_metric_ton",
        )
    )
    """
    Current prices for a metric ton of carbon removal in a currency's smallest unit.
    """
    delivery_year: typing.Optional[int] = pydantic.Field(
        alias="delivery_year", default=None
    )
    """
    The year in which the carbon removal is expected to be delivered.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object. For convenience, Climate product IDs are human-readable strings
    that start with `climsku_`. See [carbon removal inventory](https://stripe.com/docs/climate/orders/carbon-removal-inventory)
    for a list of available carbon removal products.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metric_tons_available: str = pydantic.Field(
        alias="metric_tons_available",
    )
    """
    The quantity of metric tons available for reservation.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The Climate product's name.
    """
    object: typing_extensions.Literal["climate.product"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    suppliers: typing.List[ClimateSupplier] = pydantic.Field(
        alias="suppliers",
    )
    """
    The carbon removal suppliers that fulfill orders for this Climate product.
    """
