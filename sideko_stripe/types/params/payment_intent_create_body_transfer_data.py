import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyTransferData(typing_extensions.TypedDict):
    """
    The parameters that you can use to automatically create a Transfer.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerPaymentIntentCreateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
