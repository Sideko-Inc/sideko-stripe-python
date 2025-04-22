import pydantic

from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer,
)


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransaction(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_transfer: CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer = pydantic.Field(
        alias="bank_transfer",
    )
