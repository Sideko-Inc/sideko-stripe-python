import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account


class SubscriptionTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_percent: typing.Optional[float] = pydantic.Field(
        alias="amount_percent", default=None
    )
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
    """
    destination: typing.Union[str, "Account"] = pydantic.Field(
        alias="destination",
    )
    """
    The account where funds from the payment will be transferred to upon payment success.
    """
