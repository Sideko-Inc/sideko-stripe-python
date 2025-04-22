import pydantic
import typing
import typing_extensions

from .account_bacs_debit_payments_settings import AccountBacsDebitPaymentsSettings
from .account_card_issuing_settings import AccountCardIssuingSettings
from .account_card_payments_settings import AccountCardPaymentsSettings
from .account_dashboard_settings import AccountDashboardSettings
from .account_payments_settings import AccountPaymentsSettings
from .account_payout_settings import AccountPayoutSettings
from .account_sepa_debit_payments_settings import AccountSepaDebitPaymentsSettings
from .account_treasury_settings import AccountTreasurySettings

if typing_extensions.TYPE_CHECKING:
    from .account_branding_settings import AccountBrandingSettings
    from .account_invoices_settings import AccountInvoicesSettings


class AccountSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bacs_debit_payments: typing.Optional[AccountBacsDebitPaymentsSettings] = (
        pydantic.Field(alias="bacs_debit_payments", default=None)
    )
    branding: "AccountBrandingSettings" = pydantic.Field(
        alias="branding",
    )
    card_issuing: typing.Optional[AccountCardIssuingSettings] = pydantic.Field(
        alias="card_issuing", default=None
    )
    card_payments: AccountCardPaymentsSettings = pydantic.Field(
        alias="card_payments",
    )
    dashboard: AccountDashboardSettings = pydantic.Field(
        alias="dashboard",
    )
    invoices: typing.Optional["AccountInvoicesSettings"] = pydantic.Field(
        alias="invoices", default=None
    )
    payments: AccountPaymentsSettings = pydantic.Field(
        alias="payments",
    )
    payouts: typing.Optional[AccountPayoutSettings] = pydantic.Field(
        alias="payouts", default=None
    )
    sepa_debit_payments: typing.Optional[AccountSepaDebitPaymentsSettings] = (
        pydantic.Field(alias="sepa_debit_payments", default=None)
    )
    treasury: typing.Optional[AccountTreasurySettings] = pydantic.Field(
        alias="treasury", default=None
    )
