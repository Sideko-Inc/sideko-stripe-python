import pydantic
import typing
import typing_extensions


class PaymentIntentIncrementAuthorizationBodyTransferData(typing_extensions.TypedDict):
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    amount: typing_extensions.NotRequired[int]


class _SerializerPaymentIntentIncrementAuthorizationBodyTransferData(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentIncrementAuthorizationBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
