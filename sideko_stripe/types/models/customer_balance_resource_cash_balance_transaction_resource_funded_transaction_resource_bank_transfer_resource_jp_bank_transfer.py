import pydantic
import typing


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceJpBankTransfer(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    sender_bank: typing.Optional[str] = pydantic.Field(
        alias="sender_bank", default=None
    )
    """
    The name of the bank of the sender of the funding.
    """
    sender_branch: typing.Optional[str] = pydantic.Field(
        alias="sender_branch", default=None
    )
    """
    The name of the bank branch of the sender of the funding.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    The full name of the sender, as supplied by the sending bank.
    """
