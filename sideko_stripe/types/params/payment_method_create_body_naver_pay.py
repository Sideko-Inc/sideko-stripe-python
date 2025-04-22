import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyNaverPay(typing_extensions.TypedDict):
    """
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    """

    funding: typing_extensions.NotRequired[typing_extensions.Literal["card", "points"]]


class _SerializerPaymentMethodCreateBodyNaverPay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyNaverPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    funding: typing.Optional[typing_extensions.Literal["card", "points"]] = (
        pydantic.Field(alias="funding", default=None)
    )
