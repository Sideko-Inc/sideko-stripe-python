import pydantic

from .address import Address


class FundingInstructionsBankTransferSpeiRecord(pydantic.BaseModel):
    """
    SPEI Records contain Mexico bank account details per the SPEI format.
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
    bank_address: Address = pydantic.Field(
        alias="bank_address",
    )
    bank_code: str = pydantic.Field(
        alias="bank_code",
    )
    """
    The three-digit bank code
    """
    bank_name: str = pydantic.Field(
        alias="bank_name",
    )
    """
    The short banking institution name
    """
    clabe: str = pydantic.Field(
        alias="clabe",
    )
    """
    The CLABE number
    """
