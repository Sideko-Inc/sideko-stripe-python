import pydantic
import typing_extensions


class ShippingRateDeliveryEstimateBound(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    unit: typing_extensions.Literal["business_day", "day", "hour", "month", "week"] = (
        pydantic.Field(
            alias="unit",
        )
    )
    """
    A unit of time.
    """
    value: int = pydantic.Field(
        alias="value",
    )
    """
    Must be greater than 0.
    """
