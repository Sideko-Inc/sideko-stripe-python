import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0
    """

    expires_after_days: typing_extensions.NotRequired[int]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0 handling case conversions
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
