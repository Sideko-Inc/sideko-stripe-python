import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataRadarOptions(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataRadarOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
