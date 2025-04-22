import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataNaverPay(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataNaverPay
    """

    funding: typing_extensions.NotRequired[typing_extensions.Literal["card", "points"]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataNaverPay(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataNaverPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    funding: typing.Optional[typing_extensions.Literal["card", "points"]] = (
        pydantic.Field(alias="funding", default=None)
    )
