import pydantic
import typing


class SourceTransactionChfCreditTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Reference associated with the transfer.
    """
    sender_address_country: typing.Optional[str] = pydantic.Field(
        alias="sender_address_country", default=None
    )
    """
    Sender's country address.
    """
    sender_address_line1: typing.Optional[str] = pydantic.Field(
        alias="sender_address_line1", default=None
    )
    """
    Sender's line 1 address.
    """
    sender_iban: typing.Optional[str] = pydantic.Field(
        alias="sender_iban", default=None
    )
    """
    Sender's bank account IBAN.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    Sender's name.
    """
