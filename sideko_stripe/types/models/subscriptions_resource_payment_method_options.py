import pydantic
import typing

from .invoice_payment_method_options_acss_debit import (
    InvoicePaymentMethodOptionsAcssDebit,
)
from .invoice_payment_method_options_bancontact import (
    InvoicePaymentMethodOptionsBancontact,
)
from .invoice_payment_method_options_customer_balance import (
    InvoicePaymentMethodOptionsCustomerBalance,
)
from .invoice_payment_method_options_us_bank_account import (
    InvoicePaymentMethodOptionsUsBankAccount,
)
from .subscription_payment_method_options_card import (
    SubscriptionPaymentMethodOptionsCard,
)


class SubscriptionsResourcePaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[InvoicePaymentMethodOptionsAcssDebit] = pydantic.Field(
        alias="acss_debit", default=None
    )
    bancontact: typing.Optional[InvoicePaymentMethodOptionsBancontact] = pydantic.Field(
        alias="bancontact", default=None
    )
    card: typing.Optional[SubscriptionPaymentMethodOptionsCard] = pydantic.Field(
        alias="card", default=None
    )
    customer_balance: typing.Optional[InvoicePaymentMethodOptionsCustomerBalance] = (
        pydantic.Field(alias="customer_balance", default=None)
    )
    konbini: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="konbini", default=None
    )
    sepa_debit: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    us_bank_account: typing.Optional[InvoicePaymentMethodOptionsUsBankAccount] = (
        pydantic.Field(alias="us_bank_account", default=None)
    )
