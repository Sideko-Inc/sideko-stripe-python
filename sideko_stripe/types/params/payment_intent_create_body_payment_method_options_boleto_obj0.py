import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0
    """

    expires_after_days: typing_extensions.NotRequired[int]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expires_after_days: typing.Optional[int] = pydantic.Field(
        alias="expires_after_days", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
