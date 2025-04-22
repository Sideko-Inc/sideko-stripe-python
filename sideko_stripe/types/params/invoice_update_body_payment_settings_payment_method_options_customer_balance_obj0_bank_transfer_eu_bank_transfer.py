import pydantic
import typing_extensions


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    """

    country: typing_extensions.Required[str]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
