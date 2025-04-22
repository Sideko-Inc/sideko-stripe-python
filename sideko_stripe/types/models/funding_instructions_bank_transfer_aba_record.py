import pydantic

from .address import Address


class FundingInstructionsBankTransferAbaRecord(pydantic.BaseModel):
    """
    ABA Records contain U.S. bank account details per the ABA format.
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
    The account holder name
    """
    account_number: str = pydantic.Field(
        alias="account_number",
    )
    """
    The ABA account number
    """
    account_type: str = pydantic.Field(
        alias="account_type",
    )
    """
    The account type
    """
    bank_address: Address = pydantic.Field(
        alias="bank_address",
    )
    bank_name: str = pydantic.Field(
        alias="bank_name",
    )
    """
    The bank name
    """
    routing_number: str = pydantic.Field(
        alias="routing_number",
    )
    """
    The ABA routing number
    """
