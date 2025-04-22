import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataNaverPay(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataNaverPay
    """

    funding: typing_extensions.NotRequired[typing_extensions.Literal["card", "points"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataNaverPay(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataNaverPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    funding: typing.Optional[typing_extensions.Literal["card", "points"]] = (
        pydantic.Field(alias="funding", default=None)
    )
