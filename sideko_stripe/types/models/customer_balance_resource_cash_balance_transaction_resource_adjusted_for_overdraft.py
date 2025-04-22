import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .customer_cash_balance_transaction import CustomerCashBalanceTransaction


class CustomerBalanceResourceCashBalanceTransactionResourceAdjustedForOverdraft(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    balance_transaction: typing.Union[str, "BalanceTransaction"] = pydantic.Field(
        alias="balance_transaction",
    )
    """
    The [Balance Transaction](https://stripe.com/docs/api/balance_transactions/object) that corresponds to funds taken out of your Stripe balance.
    """
    linked_transaction: typing.Union[str, "CustomerCashBalanceTransaction"] = (
        pydantic.Field(
            alias="linked_transaction",
        )
    )
    """
    The [Cash Balance Transaction](https://stripe.com/docs/api/cash_balance_transactions/object) that brought the customer balance negative, triggering the clawback of funds.
    """
