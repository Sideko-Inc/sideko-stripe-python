import pydantic
import typing

from .address import Address


class FundingInstructionsBankTransferZenginRecord(pydantic.BaseModel):
    """
    Zengin Records contain Japan bank account details per the Zengin format.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_address: Address = pydantic.Field(
        alias="account_holder_address",
    )
    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    """
    The account holder name
    """
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    """
    The account number
    """
    account_type: typing.Optional[str] = pydantic.Field(
        alias="account_type", default=None
    )
    """
    The bank account type. In Japan, this can only be `futsu` or `toza`.
    """
    bank_address: Address = pydantic.Field(
        alias="bank_address",
    )
    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    """
    The bank code of the account
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    The bank name of the account
    """
    branch_code: typing.Optional[str] = pydantic.Field(
        alias="branch_code", default=None
    )
    """
    The branch code of the account
    """
    branch_name: typing.Optional[str] = pydantic.Field(
        alias="branch_name", default=None
    )
    """
    The branch name of the account
    """
