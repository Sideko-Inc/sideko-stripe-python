import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
