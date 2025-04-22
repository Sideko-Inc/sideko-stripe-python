import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction


class CustomerBalanceResourceCashBalanceTransactionResourceTransferredToBalance(
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
    The [Balance Transaction](https://stripe.com/docs/api/balance_transactions/object) that corresponds to funds transferred to your Stripe balance.
    """
