import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account


class TransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The amount transferred to the destination account. This transfer will occur automatically after the payment succeeds. If no amount is specified, by default the entire payment amount is transferred to the destination account.
     The amount must be less than or equal to the [amount](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-amount), and must be a positive integer
     representing how much to transfer in the smallest currency unit (e.g., 100 cents to charge $1.00).
    """
    destination: typing.Union[str, "Account"] = pydantic.Field(
        alias="destination",
    )
    """
    The account (if any) that the payment is attributed to for tax reporting, and where funds from the payment are transferred to after payment success.
    """
