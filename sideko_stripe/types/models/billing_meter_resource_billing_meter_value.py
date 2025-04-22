import pydantic


class BillingMeterResourceBillingMeterValue(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_payload_key: str = pydantic.Field(
        alias="event_payload_key",
    )
    """
    The key in the meter event payload to use as the value for this meter.
    """
