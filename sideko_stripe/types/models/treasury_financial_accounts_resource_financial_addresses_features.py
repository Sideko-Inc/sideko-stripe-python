import pydantic
import typing

from .treasury_financial_accounts_resource_aba_toggle_settings import (
    TreasuryFinancialAccountsResourceAbaToggleSettings,
)


class TreasuryFinancialAccountsResourceFinancialAddressesFeatures(pydantic.BaseModel):
    """
    Settings related to Financial Addresses features on a Financial Account
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    aba: typing.Optional[TreasuryFinancialAccountsResourceAbaToggleSettings] = (
        pydantic.Field(alias="aba", default=None)
    )
    """
    Toggle settings for enabling/disabling the ABA address feature
    """
