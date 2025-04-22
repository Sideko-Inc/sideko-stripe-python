import pydantic
import typing


class SourceTransactionSepaCreditTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Reference associated with the transfer.
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
