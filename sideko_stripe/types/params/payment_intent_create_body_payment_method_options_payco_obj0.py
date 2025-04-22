import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
