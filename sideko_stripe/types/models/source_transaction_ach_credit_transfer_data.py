import pydantic
import typing


class SourceTransactionAchCreditTransferData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_data: typing.Optional[str] = pydantic.Field(
        alias="customer_data", default=None
    )
    """
    Customer data associated with the transfer.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Bank account fingerprint associated with the transfer.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last 4 digits of the account number associated with the transfer.
    """
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    Routing number associated with the transfer.
    """
