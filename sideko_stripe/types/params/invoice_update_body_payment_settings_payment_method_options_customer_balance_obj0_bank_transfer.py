import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer_eu_bank_transfer import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ]

    type_: typing_extensions.NotRequired[str]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
