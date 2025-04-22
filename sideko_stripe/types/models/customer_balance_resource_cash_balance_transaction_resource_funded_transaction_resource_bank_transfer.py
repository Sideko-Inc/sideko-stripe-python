import pydantic
import typing
import typing_extensions

from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_eu_bank_transfer import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer,
)
from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_gb_bank_transfer import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceGbBankTransfer,
)
from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_jp_bank_transfer import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceJpBankTransfer,
)
from .customer_balance_resource_cash_balance_transaction_resource_funded_transaction_resource_bank_transfer_resource_us_bank_transfer import (
    CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceUsBankTransfer,
)


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransfer(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    gb_bank_transfer: typing.Optional[
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceGbBankTransfer
    ] = pydantic.Field(alias="gb_bank_transfer", default=None)
    jp_bank_transfer: typing.Optional[
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceJpBankTransfer
    ] = pydantic.Field(alias="jp_bank_transfer", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    The user-supplied reference field on the bank transfer.
    """
    type_: typing_extensions.Literal[
        "eu_bank_transfer",
        "gb_bank_transfer",
        "jp_bank_transfer",
        "mx_bank_transfer",
        "us_bank_transfer",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """
    us_bank_transfer: typing.Optional[
        CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceUsBankTransfer
    ] = pydantic.Field(alias="us_bank_transfer", default=None)
