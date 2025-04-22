import pydantic
import typing
import typing_extensions

from .transfer_reversal_metadata import TransferReversalMetadata

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .refund import Refund
    from .transfer import Transfer


class TransferReversal(pydantic.BaseModel):
    """
    [Stripe Connect](https://stripe.com/docs/connect) platforms can reverse transfers made to a
    connected account, either entirely or partially, and can also specify whether
    to refund any related application fees. Transfer reversals add to the
    platform's balance and subtract from the destination account's balance.

    Reversing a transfer that was made for a [destination
    charge](/docs/connect/destination-charges) is allowed only up to the amount of
    the charge. It is possible to reverse a
    [transfer_group](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options)
    transfer only if the destination account has enough balance to cover the
    reversal.

    Related guide: [Reverse transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#reverse-transfers)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount, in cents (or local equivalent).
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    Balance transaction that describes the impact on your account balance.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    destination_payment_refund: typing.Optional[typing.Union[str, "Refund"]] = (
        pydantic.Field(alias="destination_payment_refund", default=None)
    )
    """
    Linked payment refund for the transfer reversal.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    metadata: typing.Optional[TransferReversalMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["transfer_reversal"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    source_refund: typing.Optional[typing.Union[str, "Refund"]] = pydantic.Field(
        alias="source_refund", default=None
    )
    """
    ID of the refund responsible for the transfer reversal.
    """
    transfer: typing.Union[str, "Transfer"] = pydantic.Field(
        alias="transfer",
    )
    """
    ID of the transfer that was reversed.
    """
