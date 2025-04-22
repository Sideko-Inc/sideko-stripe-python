import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyTransferData(typing_extensions.TypedDict):
    """
    Use this parameter to automatically create a Transfer when the payment succeeds. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    amount: typing_extensions.NotRequired[int]


class _SerializerPaymentIntentUpdateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
