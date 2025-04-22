import pydantic
import typing
import typing_extensions

from .subscription_create_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .subscription_create_body_payment_settings_payment_method_options_bancontact_obj0 import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .subscription_create_body_payment_settings_payment_method_options_card_obj0 import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .subscription_create_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .subscription_create_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class SubscriptionCreateBodyPaymentSettingsPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0, str
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0, str
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str
        ]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionCreateBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
