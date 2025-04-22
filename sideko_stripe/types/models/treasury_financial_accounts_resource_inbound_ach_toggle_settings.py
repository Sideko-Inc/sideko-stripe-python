import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_resource_toggles_setting_status_details import (
    TreasuryFinancialAccountsResourceTogglesSettingStatusDetails,
)


class TreasuryFinancialAccountsResourceInboundAchToggleSettings(pydantic.BaseModel):
    """
    Toggle settings for enabling/disabling an inbound ACH specific feature
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
    """
    Whether the FinancialAccount should have the Feature.
    """
    status: typing_extensions.Literal["active", "pending", "restricted"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    Whether the Feature is operational.
    """
    status_details: typing.List[
        TreasuryFinancialAccountsResourceTogglesSettingStatusDetails
    ] = pydantic.Field(
        alias="status_details",
    )
    """
    Additional details; includes at least one entry when the status is not `active`.
    """
