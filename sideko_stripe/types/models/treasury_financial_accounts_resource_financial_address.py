import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_resource_aba_record import (
    TreasuryFinancialAccountsResourceAbaRecord,
)


class TreasuryFinancialAccountsResourceFinancialAddress(pydantic.BaseModel):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    aba: typing.Optional[TreasuryFinancialAccountsResourceAbaRecord] = pydantic.Field(
        alias="aba", default=None
    )
    """
    ABA Records contain U.S. bank account details per the ABA format.
    """
    supported_networks: typing.Optional[
        typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]]
    ] = pydantic.Field(alias="supported_networks", default=None)
    """
    The list of networks that the address supports
    """
    type_: typing_extensions.Literal["aba"] = pydantic.Field(
        alias="type",
    )
    """
    The type of financial address
    """
