import pydantic
import typing
import typing_extensions


class BillingMeterEventCreateBodyPayload(typing_extensions.TypedDict, total=False):
    """
    The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
    """


class _SerializerBillingMeterEventCreateBodyPayload(pydantic.BaseModel):
    """
    Serializer for BillingMeterEventCreateBodyPayload handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
