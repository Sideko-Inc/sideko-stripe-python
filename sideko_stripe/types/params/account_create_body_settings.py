import pydantic
import typing
import typing_extensions

from .account_create_body_settings_bacs_debit_payments import (
    AccountCreateBodySettingsBacsDebitPayments,
    _SerializerAccountCreateBodySettingsBacsDebitPayments,
)
from .account_create_body_settings_branding import (
    AccountCreateBodySettingsBranding,
    _SerializerAccountCreateBodySettingsBranding,
)
from .account_create_body_settings_card_issuing import (
    AccountCreateBodySettingsCardIssuing,
    _SerializerAccountCreateBodySettingsCardIssuing,
)
from .account_create_body_settings_card_payments import (
    AccountCreateBodySettingsCardPayments,
    _SerializerAccountCreateBodySettingsCardPayments,
)
from .account_create_body_settings_invoices import (
    AccountCreateBodySettingsInvoices,
    _SerializerAccountCreateBodySettingsInvoices,
)
from .account_create_body_settings_payments import (
    AccountCreateBodySettingsPayments,
    _SerializerAccountCreateBodySettingsPayments,
)
from .account_create_body_settings_payouts import (
    AccountCreateBodySettingsPayouts,
    _SerializerAccountCreateBodySettingsPayouts,
)
from .account_create_body_settings_treasury import (
    AccountCreateBodySettingsTreasury,
    _SerializerAccountCreateBodySettingsTreasury,
)


class AccountCreateBodySettings(typing_extensions.TypedDict):
    """
    Options for customizing how the account functions within Stripe.
    """

    bacs_debit_payments: typing_extensions.NotRequired[
        AccountCreateBodySettingsBacsDebitPayments
    ]

    branding: typing_extensions.NotRequired[AccountCreateBodySettingsBranding]

    card_issuing: typing_extensions.NotRequired[AccountCreateBodySettingsCardIssuing]

    card_payments: typing_extensions.NotRequired[AccountCreateBodySettingsCardPayments]

    invoices: typing_extensions.NotRequired[AccountCreateBodySettingsInvoices]

    payments: typing_extensions.NotRequired[AccountCreateBodySettingsPayments]

    payouts: typing_extensions.NotRequired[AccountCreateBodySettingsPayouts]

    treasury: typing_extensions.NotRequired[AccountCreateBodySettingsTreasury]


class _SerializerAccountCreateBodySettings(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bacs_debit_payments: typing.Optional[
        _SerializerAccountCreateBodySettingsBacsDebitPayments
    ] = pydantic.Field(alias="bacs_debit_payments", default=None)
    branding: typing.Optional[_SerializerAccountCreateBodySettingsBranding] = (
        pydantic.Field(alias="branding", default=None)
    )
    card_issuing: typing.Optional[_SerializerAccountCreateBodySettingsCardIssuing] = (
        pydantic.Field(alias="card_issuing", default=None)
    )
    card_payments: typing.Optional[_SerializerAccountCreateBodySettingsCardPayments] = (
        pydantic.Field(alias="card_payments", default=None)
    )
    invoices: typing.Optional[_SerializerAccountCreateBodySettingsInvoices] = (
        pydantic.Field(alias="invoices", default=None)
    )
    payments: typing.Optional[_SerializerAccountCreateBodySettingsPayments] = (
        pydantic.Field(alias="payments", default=None)
    )
    payouts: typing.Optional[_SerializerAccountCreateBodySettingsPayouts] = (
        pydantic.Field(alias="payouts", default=None)
    )
    treasury: typing.Optional[_SerializerAccountCreateBodySettingsTreasury] = (
        pydantic.Field(alias="treasury", default=None)
    )
