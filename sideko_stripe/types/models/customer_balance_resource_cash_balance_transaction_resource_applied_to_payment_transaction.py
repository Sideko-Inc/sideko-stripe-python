import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .payment_intent import PaymentIntent


class CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_intent: typing.Union[str, "PaymentIntent"] = pydantic.Field(
        alias="payment_intent",
    )
    """
    The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were applied to.
    """
