import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .charge import Charge
    from .payment_intent import PaymentIntent


class InvoicesPaymentsInvoicePaymentAssociatedPayment(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="charge", default=None
    )
    """
    ID of the successful charge for this payment when `type` is `charge`.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    ID of the PaymentIntent associated with this payment when `type` is `payment_intent`. Note: This property is only populated for invoices finalized on or after March 15th, 2019.
    """
    type_: typing_extensions.Literal["charge", "payment_intent"] = pydantic.Field(
        alias="type",
    )
    """
    Type of payment object associated with this invoice payment.
    """
