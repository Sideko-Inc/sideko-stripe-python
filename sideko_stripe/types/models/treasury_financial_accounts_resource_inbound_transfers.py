import pydantic
import typing

from .treasury_financial_accounts_resource_inbound_ach_toggle_settings import (
    TreasuryFinancialAccountsResourceInboundAchToggleSettings,
)


class TreasuryFinancialAccountsResourceInboundTransfers(pydantic.BaseModel):
    """
    InboundTransfers contains inbound transfers features for a FinancialAccount.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach: typing.Optional[TreasuryFinancialAccountsResourceInboundAchToggleSettings] = (
        pydantic.Field(alias="ach", default=None)
    )
    """
    Toggle settings for enabling/disabling an inbound ACH specific feature
    """
