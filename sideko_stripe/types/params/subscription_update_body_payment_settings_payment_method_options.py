import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .subscription_update_body_payment_settings_payment_method_options_bancontact_obj0 import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .subscription_update_body_payment_settings_payment_method_options_card_obj0 import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .subscription_update_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .subscription_update_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0, str
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0, str
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str
        ]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
            str,
        ]
    ]

    konbini: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    sepa_debit: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
            str,
        ]
    ] = pydantic.Field(alias="customer_balance", default=None)
    konbini: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = (
        pydantic.Field(alias="konbini", default=None)
    )
    sepa_debit: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = (
        pydantic.Field(alias="sepa_debit", default=None)
    )
    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
