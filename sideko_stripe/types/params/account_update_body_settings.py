import pydantic
import typing
import typing_extensions

from .account_update_body_settings_bacs_debit_payments import (
    AccountUpdateBodySettingsBacsDebitPayments,
    _SerializerAccountUpdateBodySettingsBacsDebitPayments,
)
from .account_update_body_settings_branding import (
    AccountUpdateBodySettingsBranding,
    _SerializerAccountUpdateBodySettingsBranding,
)
from .account_update_body_settings_card_issuing import (
    AccountUpdateBodySettingsCardIssuing,
    _SerializerAccountUpdateBodySettingsCardIssuing,
)
from .account_update_body_settings_card_payments import (
    AccountUpdateBodySettingsCardPayments,
    _SerializerAccountUpdateBodySettingsCardPayments,
)
from .account_update_body_settings_invoices import (
    AccountUpdateBodySettingsInvoices,
    _SerializerAccountUpdateBodySettingsInvoices,
)
from .account_update_body_settings_payments import (
    AccountUpdateBodySettingsPayments,
    _SerializerAccountUpdateBodySettingsPayments,
)
from .account_update_body_settings_payouts import (
    AccountUpdateBodySettingsPayouts,
    _SerializerAccountUpdateBodySettingsPayouts,
)
from .account_update_body_settings_treasury import (
    AccountUpdateBodySettingsTreasury,
    _SerializerAccountUpdateBodySettingsTreasury,
)


class AccountUpdateBodySettings(typing_extensions.TypedDict):
    """
    Options for customizing how the account functions within Stripe.
    """

    bacs_debit_payments: typing_extensions.NotRequired[
        AccountUpdateBodySettingsBacsDebitPayments
    ]

    branding: typing_extensions.NotRequired[AccountUpdateBodySettingsBranding]

    card_issuing: typing_extensions.NotRequired[AccountUpdateBodySettingsCardIssuing]

    card_payments: typing_extensions.NotRequired[AccountUpdateBodySettingsCardPayments]

    invoices: typing_extensions.NotRequired[AccountUpdateBodySettingsInvoices]

    payments: typing_extensions.NotRequired[AccountUpdateBodySettingsPayments]

    payouts: typing_extensions.NotRequired[AccountUpdateBodySettingsPayouts]

    treasury: typing_extensions.NotRequired[AccountUpdateBodySettingsTreasury]


class _SerializerAccountUpdateBodySettings(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bacs_debit_payments: typing.Optional[
        _SerializerAccountUpdateBodySettingsBacsDebitPayments
    ] = pydantic.Field(alias="bacs_debit_payments", default=None)
    branding: typing.Optional[_SerializerAccountUpdateBodySettingsBranding] = (
        pydantic.Field(alias="branding", default=None)
    )
    card_issuing: typing.Optional[_SerializerAccountUpdateBodySettingsCardIssuing] = (
        pydantic.Field(alias="card_issuing", default=None)
    )
    card_payments: typing.Optional[_SerializerAccountUpdateBodySettingsCardPayments] = (
        pydantic.Field(alias="card_payments", default=None)
    )
    invoices: typing.Optional[_SerializerAccountUpdateBodySettingsInvoices] = (
        pydantic.Field(alias="invoices", default=None)
    )
    payments: typing.Optional[_SerializerAccountUpdateBodySettingsPayments] = (
        pydantic.Field(alias="payments", default=None)
    )
    payouts: typing.Optional[_SerializerAccountUpdateBodySettingsPayouts] = (
        pydantic.Field(alias="payouts", default=None)
    )
    treasury: typing.Optional[_SerializerAccountUpdateBodySettingsTreasury] = (
        pydantic.Field(alias="treasury", default=None)
    )
