import pydantic
import typing
import typing_extensions


class PaymentIntentCaptureBodyTransferData(typing_extensions.TypedDict):
    """
    The parameters that you can use to automatically create a transfer after the payment
    is captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    amount: typing_extensions.NotRequired[int]


class _SerializerPaymentIntentCaptureBodyTransferData(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCaptureBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
