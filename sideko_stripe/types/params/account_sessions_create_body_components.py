import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_account_management import (
    AccountSessionsCreateBodyComponentsAccountManagement,
    _SerializerAccountSessionsCreateBodyComponentsAccountManagement,
)
from .account_sessions_create_body_components_account_onboarding import (
    AccountSessionsCreateBodyComponentsAccountOnboarding,
    _SerializerAccountSessionsCreateBodyComponentsAccountOnboarding,
)
from .account_sessions_create_body_components_balances import (
    AccountSessionsCreateBodyComponentsBalances,
    _SerializerAccountSessionsCreateBodyComponentsBalances,
)
from .account_sessions_create_body_components_documents import (
    AccountSessionsCreateBodyComponentsDocuments,
    _SerializerAccountSessionsCreateBodyComponentsDocuments,
)
from .account_sessions_create_body_components_financial_account import (
    AccountSessionsCreateBodyComponentsFinancialAccount,
    _SerializerAccountSessionsCreateBodyComponentsFinancialAccount,
)
from .account_sessions_create_body_components_financial_account_transactions import (
    AccountSessionsCreateBodyComponentsFinancialAccountTransactions,
    _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactions,
)
from .account_sessions_create_body_components_issuing_card import (
    AccountSessionsCreateBodyComponentsIssuingCard,
    _SerializerAccountSessionsCreateBodyComponentsIssuingCard,
)
from .account_sessions_create_body_components_issuing_cards_list import (
    AccountSessionsCreateBodyComponentsIssuingCardsList,
    _SerializerAccountSessionsCreateBodyComponentsIssuingCardsList,
)
from .account_sessions_create_body_components_notification_banner import (
    AccountSessionsCreateBodyComponentsNotificationBanner,
    _SerializerAccountSessionsCreateBodyComponentsNotificationBanner,
)
from .account_sessions_create_body_components_payment_details import (
    AccountSessionsCreateBodyComponentsPaymentDetails,
    _SerializerAccountSessionsCreateBodyComponentsPaymentDetails,
)
from .account_sessions_create_body_components_payments import (
    AccountSessionsCreateBodyComponentsPayments,
    _SerializerAccountSessionsCreateBodyComponentsPayments,
)
from .account_sessions_create_body_components_payouts import (
    AccountSessionsCreateBodyComponentsPayouts,
    _SerializerAccountSessionsCreateBodyComponentsPayouts,
)
from .account_sessions_create_body_components_payouts_list import (
    AccountSessionsCreateBodyComponentsPayoutsList,
    _SerializerAccountSessionsCreateBodyComponentsPayoutsList,
)
from .account_sessions_create_body_components_tax_registrations import (
    AccountSessionsCreateBodyComponentsTaxRegistrations,
    _SerializerAccountSessionsCreateBodyComponentsTaxRegistrations,
)
from .account_sessions_create_body_components_tax_settings import (
    AccountSessionsCreateBodyComponentsTaxSettings,
    _SerializerAccountSessionsCreateBodyComponentsTaxSettings,
)


class AccountSessionsCreateBodyComponents(typing_extensions.TypedDict):
    """
    Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
    """

    account_management: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsAccountManagement
    ]

    account_onboarding: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsAccountOnboarding
    ]

    balances: typing_extensions.NotRequired[AccountSessionsCreateBodyComponentsBalances]

    documents: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsDocuments
    ]

    financial_account: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsFinancialAccount
    ]

    financial_account_transactions: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsFinancialAccountTransactions
    ]

    issuing_card: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsIssuingCard
    ]

    issuing_cards_list: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsIssuingCardsList
    ]

    notification_banner: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsNotificationBanner
    ]

    payment_details: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsPaymentDetails
    ]

    payments: typing_extensions.NotRequired[AccountSessionsCreateBodyComponentsPayments]

    payouts: typing_extensions.NotRequired[AccountSessionsCreateBodyComponentsPayouts]

    payouts_list: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsPayoutsList
    ]

    tax_registrations: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsTaxRegistrations
    ]

    tax_settings: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsTaxSettings
    ]


class _SerializerAccountSessionsCreateBodyComponents(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponents handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_management: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsAccountManagement
    ] = pydantic.Field(alias="account_management", default=None)
    account_onboarding: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsAccountOnboarding
    ] = pydantic.Field(alias="account_onboarding", default=None)
    balances: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsBalances
    ] = pydantic.Field(alias="balances", default=None)
    documents: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsDocuments
    ] = pydantic.Field(alias="documents", default=None)
    financial_account: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsFinancialAccount
    ] = pydantic.Field(alias="financial_account", default=None)
    financial_account_transactions: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactions
    ] = pydantic.Field(alias="financial_account_transactions", default=None)
    issuing_card: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsIssuingCard
    ] = pydantic.Field(alias="issuing_card", default=None)
    issuing_cards_list: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsIssuingCardsList
    ] = pydantic.Field(alias="issuing_cards_list", default=None)
    notification_banner: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsNotificationBanner
    ] = pydantic.Field(alias="notification_banner", default=None)
    payment_details: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPaymentDetails
    ] = pydantic.Field(alias="payment_details", default=None)
    payments: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPayments
    ] = pydantic.Field(alias="payments", default=None)
    payouts: typing.Optional[_SerializerAccountSessionsCreateBodyComponentsPayouts] = (
        pydantic.Field(alias="payouts", default=None)
    )
    payouts_list: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPayoutsList
    ] = pydantic.Field(alias="payouts_list", default=None)
    tax_registrations: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsTaxRegistrations
    ] = pydantic.Field(alias="tax_registrations", default=None)
    tax_settings: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsTaxSettings
    ] = pydantic.Field(alias="tax_settings", default=None)
