import pydantic

from .address import Address


class FundingInstructionsBankTransferSortCodeRecord(pydantic.BaseModel):
    """
    Sort Code Records contain U.K. bank account details per the sort code format.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_address: Address = pydantic.Field(
        alias="account_holder_address",
    )
    account_holder_name: str = pydantic.Field(
        alias="account_holder_name",
    )
    """
    The name of the person or business that owns the bank account
    """
    account_number: str = pydantic.Field(
        alias="account_number",
    )
    """
    The account number
    """
    bank_address: Address = pydantic.Field(
        alias="bank_address",
    )
    sort_code: str = pydantic.Field(
        alias="sort_code",
    )
    """
    The six-digit sort code
    """
