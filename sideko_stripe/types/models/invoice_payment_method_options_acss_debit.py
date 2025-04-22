import pydantic
import typing
import typing_extensions

from .invoice_payment_method_options_acss_debit_mandate_options import (
    InvoicePaymentMethodOptionsAcssDebitMandateOptions,
)


class InvoicePaymentMethodOptionsAcssDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        InvoicePaymentMethodOptionsAcssDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
