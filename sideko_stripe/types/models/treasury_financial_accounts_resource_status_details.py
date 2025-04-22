import pydantic
import typing

from .treasury_financial_accounts_resource_closed_status_details import (
    TreasuryFinancialAccountsResourceClosedStatusDetails,
)


class TreasuryFinancialAccountsResourceStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    closed: typing.Optional[TreasuryFinancialAccountsResourceClosedStatusDetails] = (
        pydantic.Field(alias="closed", default=None)
    )
