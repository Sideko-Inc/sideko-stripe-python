import pydantic
import typing
import typing_extensions

from .invoice_create_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .invoice_create_body_payment_settings_payment_method_options_bancontact_obj0 import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .invoice_create_body_payment_settings_payment_method_options_card_obj0 import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .invoice_create_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .invoice_create_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class InvoiceCreateBodyPaymentSettingsPaymentMethodOptions(typing_extensions.TypedDict):
    """
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0, str
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0, str
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0, str
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
            InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0, str
        ]
    ]


class _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
