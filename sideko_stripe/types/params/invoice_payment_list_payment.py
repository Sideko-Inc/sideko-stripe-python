import pydantic
import typing
import typing_extensions


class InvoicePaymentListPayment(typing_extensions.TypedDict):
    """
    The payment details of the invoice payments to return.
    """

    payment_intent: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["payment_intent"]]


class _SerializerInvoicePaymentListPayment(pydantic.BaseModel):
    """
    Serializer for InvoicePaymentListPayment handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payment_intent: typing.Optional[str] = pydantic.Field(
        alias="payment_intent", default=None
    )
    type_: typing_extensions.Literal["payment_intent"] = pydantic.Field(
        alias="type",
    )
