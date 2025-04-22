import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyRadarOptions(typing_extensions.TypedDict):
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """

    session: typing_extensions.NotRequired[str]


class _SerializerPaymentMethodCreateBodyRadarOptions(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
