import pydantic
import typing

from .invoice_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer import (
    InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
)


class InvoicePaymentMethodOptionsCustomerBalanceBankTransfer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        InvoicePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """
