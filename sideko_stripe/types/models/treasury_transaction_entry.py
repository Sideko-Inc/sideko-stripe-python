import pydantic
import typing
import typing_extensions

from .treasury_transactions_resource_balance_impact import (
    TreasuryTransactionsResourceBalanceImpact,
)

if typing_extensions.TYPE_CHECKING:
    from .treasury_transaction import TreasuryTransaction
    from .treasury_transactions_resource_flow_details import (
        TreasuryTransactionsResourceFlowDetails,
    )


class TreasuryTransactionEntry(pydantic.BaseModel):
    """
    TransactionEntries represent individual units of money movements within a single [Transaction](https://stripe.com/docs/api#transactions).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
    effective_at: int = pydantic.Field(
        alias="effective_at",
    )
    """
    When the TransactionEntry will impact the FinancialAccount's balance.
    """
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    """
    The FinancialAccount associated with this object.
    """
    flow: typing.Optional[str] = pydantic.Field(alias="flow", default=None)
    """
    Token of the flow associated with the TransactionEntry.
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
    Type of the flow associated with the TransactionEntry.
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
    object: typing_extensions.Literal["treasury.transaction_entry"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    transaction: typing.Union[str, "TreasuryTransaction"] = pydantic.Field(
        alias="transaction",
    )
    """
    The Transaction associated with this object.
    """
    type_: typing_extensions.Literal[
        "credit_reversal",
        "credit_reversal_posting",
        "debit_reversal",
        "inbound_transfer",
        "inbound_transfer_return",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "other",
        "outbound_payment",
        "outbound_payment_cancellation",
        "outbound_payment_failure",
        "outbound_payment_posting",
        "outbound_payment_return",
        "outbound_transfer",
        "outbound_transfer_cancellation",
        "outbound_transfer_failure",
        "outbound_transfer_posting",
        "outbound_transfer_return",
        "received_credit",
        "received_debit",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The specific money movement that generated the TransactionEntry.
    """
