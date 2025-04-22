import pydantic
import typing

from .climate_removals_products_price import ClimateRemovalsProductsPrice


class ClimateProductCurrentPricesPerMetricTon(pydantic.BaseModel):
    """
    Current prices for a metric ton of carbon removal in a currency's smallest unit.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, ClimateRemovalsProductsPrice]
