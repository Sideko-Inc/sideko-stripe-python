import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account


class PaymentLinksResourceTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The amount in cents (or local equivalent) that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
    """
    destination: typing.Union[str, "Account"] = pydantic.Field(
        alias="destination",
    )
    """
    The connected account receiving the transfer.
    """
