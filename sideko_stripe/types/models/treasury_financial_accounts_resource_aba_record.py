import pydantic
import typing


class TreasuryFinancialAccountsResourceAbaRecord(pydantic.BaseModel):
    """
    ABA Records contain U.S. bank account details per the ABA format.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_name: str = pydantic.Field(
        alias="account_holder_name",
    )
    """
    The name of the person or business that owns the bank account.
    """
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    """
    The account number.
    """
    account_number_last4: str = pydantic.Field(
        alias="account_number_last4",
    )
    """
    The last four characters of the account number.
    """
    bank_name: str = pydantic.Field(
        alias="bank_name",
    )
    """
    Name of the bank.
    """
    routing_number: str = pydantic.Field(
        alias="routing_number",
    )
    """
    Routing number for the account.
    """
