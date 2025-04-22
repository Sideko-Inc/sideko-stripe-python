import pydantic
import typing
import typing_extensions

from .invoice_payment_method_options_us_bank_account_linked_account_options import (
    InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions,
)


class InvoicePaymentMethodOptionsUsBankAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions
    ] = pydantic.Field(alias="financial_connections", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
