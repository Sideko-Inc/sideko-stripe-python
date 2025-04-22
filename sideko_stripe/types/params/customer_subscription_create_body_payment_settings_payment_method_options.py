import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .customer_subscription_create_body_payment_settings_payment_method_options_bancontact_obj0 import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .customer_subscription_create_body_payment_settings_payment_method_options_card_obj0 import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .customer_subscription_create_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .customer_subscription_create_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
