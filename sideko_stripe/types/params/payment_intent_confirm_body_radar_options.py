import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyRadarOptions(typing_extensions.TypedDict):
    """
    Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
    """

    session: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentConfirmBodyRadarOptions(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
