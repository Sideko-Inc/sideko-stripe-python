import pydantic
import typing
import typing_extensions

from .treasury_transactions_resource_abstract_transaction_resource_status_transitions import (
    TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions,
)
from .treasury_transactions_resource_balance_impact import (
    TreasuryTransactionsResourceBalanceImpact,
)

if typing_extensions.TYPE_CHECKING:
    from .treasury_transaction_entries import TreasuryTransactionEntries
    from .treasury_transactions_resource_flow_details import (
        TreasuryTransactionsResourceFlowDetails,
    )


class TreasuryTransaction(pydantic.BaseModel):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount (in cents) transferred.
    """
    balance_impact: TreasuryTransactionsResourceBalanceImpact = pydantic.Field(
        alias="balance_impact",
    )
    """
    Change to a FinancialAccount's balance
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
    description: str = pydantic.Field(
        alias="description",
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    entries: typing.Optional["TreasuryTransactionEntries"] = pydantic.Field(
        alias="entries", default=None
    )
    """
    A list of TransactionEntries that are part of this Transaction. This cannot be expanded in any list endpoints.
    """
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    """
    The FinancialAccount associated with this object.
    """
    flow: typing.Optional[str] = pydantic.Field(alias="flow", default=None)
    """
    ID of the flow that created the Transaction.
    """
    flow_details: typing.Optional["TreasuryTransactionsResourceFlowDetails"] = (
        pydantic.Field(alias="flow_details", default=None)
    )
    flow_type: typing_extensions.Literal[
        "credit_reversal",
        "debit_reversal",
        "inbound_transfer",
        "issuing_authorization",
        "other",
        "outbound_payment",
        "outbound_transfer",
        "received_credit",
        "received_debit",
    ] = pydantic.Field(
        alias="flow_type",
    )
    """
    Type of the flow that created the Transaction.
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
    object: typing_extensions.Literal["treasury.transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["open", "posted", "void"] = pydantic.Field(
        alias="status",
    )
    """
    Status of the Transaction.
    """
    status_transitions: TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions = pydantic.Field(
        alias="status_transitions",
    )
