import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .customer_subscription_modify_body_payment_settings_payment_method_options_bancontact_obj0 import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .customer_subscription_modify_body_payment_settings_payment_method_options_card_obj0 import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .customer_subscription_modify_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .customer_subscription_modify_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCardObj0,
            str,
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
