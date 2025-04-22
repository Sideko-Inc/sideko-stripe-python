import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0
    """

    app_id: typing_extensions.NotRequired[str]

    client: typing_extensions.NotRequired[
        typing_extensions.Literal["android", "ios", "web"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_id: typing.Optional[str] = pydantic.Field(alias="app_id", default=None)
    client: typing.Optional[typing_extensions.Literal["android", "ios", "web"]] = (
        pydantic.Field(alias="client", default=None)
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
