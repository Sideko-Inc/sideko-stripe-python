import pydantic
import typing


class SourceTransactionGbpCreditTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Bank account fingerprint associated with the Stripe owned bank account receiving the transfer.
    """
    funding_method: typing.Optional[str] = pydantic.Field(
        alias="funding_method", default=None
    )
    """
    The credit transfer rails the sender used to push this transfer. The possible rails are: Faster Payments, BACS, CHAPS, and wire transfers. Currently only Faster Payments is supported.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last 4 digits of sender account number associated with the transfer.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Sender entered arbitrary information about the transfer.
    """
    sender_account_number: typing.Optional[str] = pydantic.Field(
        alias="sender_account_number", default=None
    )
    """
    Sender account number associated with the transfer.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    Sender name associated with the transfer.
    """
    sender_sort_code: typing.Optional[str] = pydantic.Field(
        alias="sender_sort_code", default=None
    )
    """
    Sender sort code associated with the transfer.
    """
