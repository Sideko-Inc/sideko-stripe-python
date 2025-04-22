import pydantic
import typing
import typing_extensions

from .invoice_create_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer_eu_bank_transfer import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
)


class InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    typing_extensions.TypedDict
):
    """
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ]

    type_: typing_extensions.NotRequired[str]


class _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
