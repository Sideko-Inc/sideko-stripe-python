import pydantic
import typing


class BillingMeterResourceBillingMeterStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deactivated_at: typing.Optional[int] = pydantic.Field(
        alias="deactivated_at", default=None
    )
    """
    The time the meter was deactivated, if any. Measured in seconds since Unix epoch.
    """
