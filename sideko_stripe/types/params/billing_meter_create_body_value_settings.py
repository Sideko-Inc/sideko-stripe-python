import pydantic
import typing_extensions


class BillingMeterCreateBodyValueSettings(typing_extensions.TypedDict):
    """
    Fields that specify how to calculate a meter event's value.
    """

    event_payload_key: typing_extensions.Required[str]


class _SerializerBillingMeterCreateBodyValueSettings(pydantic.BaseModel):
    """
    Serializer for BillingMeterCreateBodyValueSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    event_payload_key: str = pydantic.Field(
        alias="event_payload_key",
    )
