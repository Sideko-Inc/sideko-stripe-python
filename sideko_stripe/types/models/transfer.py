import pydantic
import typing
import typing_extensions

from .transfer_metadata import TransferMetadata

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .balance_transaction import BalanceTransaction
    from .charge import Charge
    from .transfer_reversals import TransferReversals


class Transfer(pydantic.BaseModel):
    """
    A `Transfer` object is created when you move funds between Stripe accounts as
    part of Connect.

    Before April 6, 2017, transfers also represented movement of funds from a
    Stripe account to a card or bank account. This behavior has since been split
    out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
    information, read about the
    [transfer/payout split](https://stripe.com/docs/transfer-payout-split).

    Related guide: [Creating separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount in cents (or local equivalent) to be transferred.
    """
    amount_reversed: int = pydantic.Field(
        alias="amount_reversed",
    )
    """
    Amount in cents (or local equivalent) reversed (can be less than the amount attribute on the transfer if a partial reversal was issued).
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    Balance transaction that describes the impact of this transfer on your account balance.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time that this record of the transfer was first created.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    destination: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="destination", default=None
    )
    """
    ID of the Stripe account the transfer was sent to.
    """
    destination_payment: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="destination_payment", default=None
    )
    """
    If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: TransferMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["transfer"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reversals: "TransferReversals" = pydantic.Field(
        alias="reversals",
    )
    """
    A list of reversals that have been applied to the transfer.
    """
    reversed: bool = pydantic.Field(
        alias="reversed",
    )
    """
    Whether the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false.
    """
    source_transaction: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="source_transaction", default=None
    )
    """
    ID of the charge that was used to fund the transfer. If null, the transfer was funded from the available balance.
    """
    source_type: typing.Optional[str] = pydantic.Field(
        alias="source_type", default=None
    )
    """
    The source balance this transfer came from. One of `card`, `fpx`, or `bank_account`.
    """
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
    """
    A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """
