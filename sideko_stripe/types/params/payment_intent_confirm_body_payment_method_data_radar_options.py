import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataRadarOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataRadarOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
