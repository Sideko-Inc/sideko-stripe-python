import pydantic
import typing
import typing_extensions

from .invoice_payment_method_options_customer_balance_bank_transfer import (
    InvoicePaymentMethodOptionsCustomerBalanceBankTransfer,
)


class InvoicePaymentMethodOptionsCustomerBalance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        InvoicePaymentMethodOptionsCustomerBalanceBankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    """
    The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
    """
