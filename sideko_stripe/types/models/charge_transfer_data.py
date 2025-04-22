import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account


class ChargeTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
    """
    destination: typing.Union[str, "Account"] = pydantic.Field(
        alias="destination",
    )
    """
    ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request.
    """
