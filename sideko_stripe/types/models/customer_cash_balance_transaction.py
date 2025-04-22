import pydantic
import typing
import typing_extensions

from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction,
)

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer
    from .customer_balance_resource_cash_balance_transaction_resource_adjusted_for_overdraft import (
        CustomerBalanceResourceCashBalanceTransactionResourceAdjustedForOverdraft,
    )
    from .customer_balance_resource_cash_balance_transaction_resource_applied_to_payment_transaction import (
        CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction,
    )
    from .customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction import (
        CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction,
    )
    from .customer_balance_resource_cash_balance_transaction_resource_transferred_to_balance import (
        CustomerBalanceResourceCashBalanceTransactionResourceTransferredToBalance,
    )
    from .customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction import (
        CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction,
    )


class CustomerCashBalanceTransaction(pydantic.BaseModel):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid
    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adjusted_for_overdraft: typing.Optional[
        "CustomerBalanceResourceCashBalanceTransactionResourceAdjustedForOverdraft"
    ] = pydantic.Field(alias="adjusted_for_overdraft", default=None)
    applied_to_payment: typing.Optional[
        "CustomerBalanceResourceCashBalanceTransactionResourceAppliedToPaymentTransaction"
    ] = pydantic.Field(alias="applied_to_payment", default=None)
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
    customer: typing.Union[str, "Customer"] = pydantic.Field(
        alias="customer",
    )
    """
    The customer whose available cash balance changed as a result of this transaction.
    """
    ending_balance: int = pydantic.Field(
        alias="ending_balance",
    )
    """
    The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    funded: typing.Optional[
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction
    ] = pydantic.Field(alias="funded", default=None)
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
    net_amount: int = pydantic.Field(
        alias="net_amount",
    )
    """
    The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.
    """
    object: typing_extensions.Literal["customer_cash_balance_transaction"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    refunded_from_payment: typing.Optional[
        "CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction"
    ] = pydantic.Field(alias="refunded_from_payment", default=None)
    transferred_to_balance: typing.Optional[
        "CustomerBalanceResourceCashBalanceTransactionResourceTransferredToBalance"
    ] = pydantic.Field(alias="transferred_to_balance", default=None)
    type_: typing_extensions.Literal[
        "adjusted_for_overdraft",
        "applied_to_payment",
        "funded",
        "funding_reversed",
        "refunded_from_payment",
        "return_canceled",
        "return_initiated",
        "transferred_to_balance",
        "unapplied_from_payment",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of the cash balance transaction. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types.
    """
    unapplied_from_payment: typing.Optional[
        "CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction"
    ] = pydantic.Field(alias="unapplied_from_payment", default=None)
