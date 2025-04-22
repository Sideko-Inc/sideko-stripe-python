import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
