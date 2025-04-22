import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_acss_debit_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
)
from .invoice_update_body_payment_settings_payment_method_options_bancontact_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
)
from .invoice_update_body_payment_settings_payment_method_options_card_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0,
)
from .invoice_update_body_payment_settings_payment_method_options_customer_balance_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
)
from .invoice_update_body_payment_settings_payment_method_options_us_bank_account_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptions(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptions
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[
            InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0, str
        ]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[
            InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0, str
        ]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0, str
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
            InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0, str
        ]
    ]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0,
            str,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0,
            str,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0, str
        ]
    ] = pydantic.Field(alias="card", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0,
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
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
