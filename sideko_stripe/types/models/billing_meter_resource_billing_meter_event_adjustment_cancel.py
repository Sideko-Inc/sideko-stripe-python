import pydantic
import typing


class BillingMeterResourceBillingMeterEventAdjustmentCancel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    identifier: typing.Optional[str] = pydantic.Field(alias="identifier", default=None)
    """
    Unique identifier for the event.
    """
