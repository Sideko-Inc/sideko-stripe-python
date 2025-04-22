import pydantic
import typing_extensions

from .bank_connections_resource_transaction_resource_status_transitions import (
    BankConnectionsResourceTransactionResourceStatusTransitions,
)


class FinancialConnectionsTransaction(pydantic.BaseModel):
    """
    A Transaction represents a real transaction that affects a Financial Connections Account balance.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: str = pydantic.Field(
        alias="account",
    )
    """
    The ID of the Financial Connections Account this transaction belongs to.
    """
    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of this transaction, in cents (or local equivalent).
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
    The description of this transaction.
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
    object: typing_extensions.Literal["financial_connections.transaction"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["pending", "posted", "void"] = pydantic.Field(
        alias="status",
    )
    """
    The status of the transaction.
    """
    status_transitions: BankConnectionsResourceTransactionResourceStatusTransitions = (
        pydantic.Field(
            alias="status_transitions",
        )
    )
    transacted_at: int = pydantic.Field(
        alias="transacted_at",
    )
    """
    Time at which the transaction was transacted. Measured in seconds since the Unix epoch.
    """
    transaction_refresh: str = pydantic.Field(
        alias="transaction_refresh",
    )
    """
    The token of the transaction refresh that last updated or created this transaction.
    """
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
