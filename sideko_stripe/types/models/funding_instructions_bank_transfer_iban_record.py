import pydantic

from .address import Address


class FundingInstructionsBankTransferIbanRecord(pydantic.BaseModel):
    """
    Iban Records contain E.U. bank account details per the SEPA format.
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
    bank_address: Address = pydantic.Field(
        alias="bank_address",
    )
    bic: str = pydantic.Field(
        alias="bic",
    )
    """
    The BIC/SWIFT code of the account.
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    iban: str = pydantic.Field(
        alias="iban",
    )
    """
    The IBAN of the account.
    """
