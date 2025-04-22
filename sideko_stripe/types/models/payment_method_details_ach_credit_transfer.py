import pydantic
import typing


class PaymentMethodDetailsAchCreditTransfer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    """
    Account number to transfer funds to.
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Name of the bank associated with the routing number.
    """
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    Routing transit number for the bank account to transfer funds to.
    """
    swift_code: typing.Optional[str] = pydantic.Field(alias="swift_code", default=None)
    """
    SWIFT code of the bank associated with the routing number.
    """
