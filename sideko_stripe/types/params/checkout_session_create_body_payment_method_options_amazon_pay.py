import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
