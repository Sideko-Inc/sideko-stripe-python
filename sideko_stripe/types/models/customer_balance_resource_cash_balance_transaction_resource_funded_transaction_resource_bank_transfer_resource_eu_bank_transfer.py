import pydantic
import typing


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceEuBankTransfer(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bic: typing.Optional[str] = pydantic.Field(alias="bic", default=None)
    """
    The BIC of the bank of the sender of the funding.
    """
    iban_last4: typing.Optional[str] = pydantic.Field(alias="iban_last4", default=None)
    """
    The last 4 digits of the IBAN of the sender of the funding.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    The full name of the sender, as supplied by the sending bank.
    """
