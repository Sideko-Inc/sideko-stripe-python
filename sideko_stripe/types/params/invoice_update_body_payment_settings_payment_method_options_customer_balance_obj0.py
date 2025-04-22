import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[str]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[str] = pydantic.Field(
        alias="funding_type", default=None
    )
