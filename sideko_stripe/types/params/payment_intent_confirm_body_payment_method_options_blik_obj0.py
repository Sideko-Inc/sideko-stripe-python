import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0
    """

    code: typing_extensions.NotRequired[str]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    code: typing.Optional[str] = pydantic.Field(alias="code", default=None)
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
