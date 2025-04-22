import pydantic
import typing


class TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccount(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Bank name.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the bank account number.
    """
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    The routing number for the bank account.
    """
