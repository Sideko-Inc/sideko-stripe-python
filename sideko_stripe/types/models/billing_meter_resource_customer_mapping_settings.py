import pydantic
import typing_extensions


class BillingMeterResourceCustomerMappingSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_payload_key: str = pydantic.Field(
        alias="event_payload_key",
    )
    """
    The key in the meter event payload to use for mapping the event to a customer.
    """
    type_: typing_extensions.Literal["by_id"] = pydantic.Field(
        alias="type",
    )
    """
    The method for mapping a meter event to a customer.
    """
