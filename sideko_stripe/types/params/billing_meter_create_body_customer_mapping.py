import pydantic
import typing_extensions


class BillingMeterCreateBodyCustomerMapping(typing_extensions.TypedDict):
    """
    Fields that specify how to map a meter event to a customer.
    """

    event_payload_key: typing_extensions.Required[str]

    type_: typing_extensions.Required[typing_extensions.Literal["by_id"]]


class _SerializerBillingMeterCreateBodyCustomerMapping(pydantic.BaseModel):
    """
    Serializer for BillingMeterCreateBodyCustomerMapping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    event_payload_key: str = pydantic.Field(
        alias="event_payload_key",
    )
    type_: typing_extensions.Literal["by_id"] = pydantic.Field(
        alias="type",
    )
