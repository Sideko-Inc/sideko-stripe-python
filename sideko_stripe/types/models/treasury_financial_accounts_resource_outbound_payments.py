import pydantic
import typing

from .treasury_financial_accounts_resource_outbound_ach_toggle_settings import (
    TreasuryFinancialAccountsResourceOutboundAchToggleSettings,
)
from .treasury_financial_accounts_resource_toggle_settings import (
    TreasuryFinancialAccountsResourceToggleSettings,
)


class TreasuryFinancialAccountsResourceOutboundPayments(pydantic.BaseModel):
    """
    Settings related to Outbound Payments features on a Financial Account
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach: typing.Optional[TreasuryFinancialAccountsResourceOutboundAchToggleSettings] = (
        pydantic.Field(alias="ach", default=None)
    )
    """
    Toggle settings for enabling/disabling an outbound ACH specific feature
    """
    us_domestic_wire: typing.Optional[
        TreasuryFinancialAccountsResourceToggleSettings
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
    """
    Toggle settings for enabling/disabling a feature
    """
