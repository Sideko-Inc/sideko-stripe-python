import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsPixObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsPixObj0
    """

    expires_after_seconds: typing_extensions.NotRequired[int]

    expires_at: typing_extensions.NotRequired[int]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPixObj0(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsPixObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expires_after_seconds: typing.Optional[int] = pydantic.Field(
        alias="expires_after_seconds", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
