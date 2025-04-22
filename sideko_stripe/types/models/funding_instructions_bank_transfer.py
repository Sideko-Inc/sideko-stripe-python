import pydantic
import typing
import typing_extensions

from .funding_instructions_bank_transfer_financial_address import (
    FundingInstructionsBankTransferFinancialAddress,
)


class FundingInstructionsBankTransfer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
    """
    The country of the bank account to fund
    """
    financial_addresses: typing.List[
        FundingInstructionsBankTransferFinancialAddress
    ] = pydantic.Field(
        alias="financial_addresses",
    )
    """
    A list of financial addresses that can be used to fund a particular balance
    """
    type_: typing_extensions.Literal["eu_bank_transfer", "jp_bank_transfer"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The bank_transfer type
    """
