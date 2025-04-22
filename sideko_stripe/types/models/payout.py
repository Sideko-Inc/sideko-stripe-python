import pydantic
import typing
import typing_extensions

from .deleted_bank_account import DeletedBankAccount
from .deleted_card import DeletedCard
from .payout_metadata import PayoutMetadata
from .payouts_trace_id import PayoutsTraceId

if typing_extensions.TYPE_CHECKING:
    from .application_fee import ApplicationFee
    from .balance_transaction import BalanceTransaction
    from .bank_account import BankAccount
    from .card import Card


class Payout(pydantic.BaseModel):
    """
    A `Payout` object is created when you receive funds from Stripe, or when you
    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    and list all payouts. Payouts are made on [varying
    schedules](/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving payouts](https://stripe.com/docs/payouts)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount (in cents (or local equivalent)) that transfers to your bank account or debit card.
    """
    application_fee: typing.Optional[typing.Union[str, "ApplicationFee"]] = (
        pydantic.Field(alias="application_fee", default=None)
    )
    """
    The application fee (if any) for the payout. [See the Connect documentation](https://stripe.com/docs/connect/instant-payouts#monetization-and-fees) for details.
    """
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    """
    The amount of the application fee (if any) requested for the payout. [See the Connect documentation](https://stripe.com/docs/connect/instant-payouts#monetization-and-fees) for details.
    """
    arrival_date: int = pydantic.Field(
        alias="arrival_date",
    )
    """
    Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.
    """
    automatic: bool = pydantic.Field(
        alias="automatic",
    )
    """
    Returns `true` if the payout is created by an [automated payout schedule](https://stripe.com/docs/payouts#payout-schedule) and `false` if it's [requested manually](https://stripe.com/docs/payouts#manual-payouts).
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    ID of the balance transaction that describes the impact of this payout on your account balance.
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
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    destination: typing.Optional[
        typing.Union[str, "BankAccount", "Card", DeletedBankAccount, DeletedCard]
    ] = pydantic.Field(alias="destination", default=None)
    """
    ID of the bank account or card the payout is sent to.
    """
    failure_balance_transaction: typing.Optional[
        typing.Union[str, "BalanceTransaction"]
    ] = pydantic.Field(alias="failure_balance_transaction", default=None)
    """
    If the payout fails or cancels, this is the ID of the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance.
    """
    failure_code: typing.Optional[str] = pydantic.Field(
        alias="failure_code", default=None
    )
    """
    Error code that provides a reason for a payout failure, if available. View our [list of failure codes](https://stripe.com/docs/api#payout_failures).
    """
    failure_message: typing.Optional[str] = pydantic.Field(
        alias="failure_message", default=None
    )
    """
    Message that provides the reason for a payout failure, if available.
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
    metadata: typing.Optional[PayoutMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    method: str = pydantic.Field(
        alias="method",
    )
    """
    The method used to send this payout, which can be `standard` or `instant`. `instant` is supported for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
    """
    object: typing_extensions.Literal["payout"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    original_payout: typing.Optional[typing.Union[str, "Payout"]] = pydantic.Field(
        alias="original_payout", default=None
    )
    """
    If the payout reverses another, this is the ID of the original payout.
    """
    reconciliation_status: typing_extensions.Literal[
        "completed", "in_progress", "not_applicable"
    ] = pydantic.Field(
        alias="reconciliation_status",
    )
    """
    If `completed`, you can use the [Balance Transactions API](https://stripe.com/docs/api/balance_transactions/list#balance_transaction_list-payout) to list all balance transactions that are paid out in this payout.
    """
    reversed_by: typing.Optional[typing.Union[str, "Payout"]] = pydantic.Field(
        alias="reversed_by", default=None
    )
    """
    If the payout reverses, this is the ID of the payout that reverses this payout.
    """
    source_type: str = pydantic.Field(
        alias="source_type",
    )
    """
    The source balance this payout came from, which can be one of the following: `card`, `fpx`, or `bank_account`.
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    Extra information about a payout that displays on the user's bank statement.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it's submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`.
    """
    trace_id: typing.Optional[PayoutsTraceId] = pydantic.Field(
        alias="trace_id", default=None
    )
    type_: typing_extensions.Literal["bank_account", "card"] = pydantic.Field(
        alias="type",
    )
    """
    Can be `bank_account` or `card`.
    """
