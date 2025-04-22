import pydantic
import typing


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceGbBankTransfer(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number_last4: typing.Optional[str] = pydantic.Field(
        alias="account_number_last4", default=None
    )
    """
    The last 4 digits of the account number of the sender of the funding.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    The full name of the sender, as supplied by the sending bank.
    """
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
    """
    The sort code of the bank of the sender of the funding
    """
