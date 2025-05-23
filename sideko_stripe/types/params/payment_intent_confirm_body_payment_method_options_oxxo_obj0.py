import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0
    """

    expires_after_days: typing_extensions.NotRequired[int]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expires_after_days: typing.Optional[int] = pydantic.Field(
        alias="expires_after_days", default=None
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
