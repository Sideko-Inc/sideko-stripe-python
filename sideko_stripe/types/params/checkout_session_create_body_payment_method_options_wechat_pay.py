import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsWechatPay(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsWechatPay
    """

    app_id: typing_extensions.NotRequired[str]

    client: typing_extensions.Required[
        typing_extensions.Literal["android", "ios", "web"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsWechatPay(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsWechatPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_id: typing.Optional[str] = pydantic.Field(alias="app_id", default=None)
    client: typing_extensions.Literal["android", "ios", "web"] = pydantic.Field(
        alias="client",
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
