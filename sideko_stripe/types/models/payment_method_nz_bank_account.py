import pydantic
import typing


class PaymentMethodNzBankAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    """
    The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod’s billing details.
    """
    bank_code: str = pydantic.Field(
        alias="bank_code",
    )
    """
    The numeric code for the bank account's bank.
    """
    bank_name: str = pydantic.Field(
        alias="bank_name",
    )
    """
    The name of the bank.
    """
    branch_code: str = pydantic.Field(
        alias="branch_code",
    )
    """
    The numeric code for the bank account's bank branch.
    """
    last4: str = pydantic.Field(
        alias="last4",
    )
    """
    Last four digits of the bank account number.
    """
    suffix: typing.Optional[str] = pydantic.Field(alias="suffix", default=None)
    """
    The suffix of the bank account number.
    """
