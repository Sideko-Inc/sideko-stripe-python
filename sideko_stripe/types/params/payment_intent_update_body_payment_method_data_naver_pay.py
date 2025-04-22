import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodDataNaverPay(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodDataNaverPay
    """

    funding: typing_extensions.NotRequired[typing_extensions.Literal["card", "points"]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataNaverPay(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataNaverPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    funding: typing.Optional[typing_extensions.Literal["card", "points"]] = (
        pydantic.Field(alias="funding", default=None)
    )
