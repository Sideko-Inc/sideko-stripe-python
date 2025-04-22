import pydantic
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .payment_pages_checkout_session_invoice_settings import (
        PaymentPagesCheckoutSessionInvoiceSettings,
    )


class PaymentPagesCheckoutSessionInvoiceCreation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether invoice creation is enabled for the Checkout Session.
    """
    invoice_data: "PaymentPagesCheckoutSessionInvoiceSettings" = pydantic.Field(
        alias="invoice_data",
    )
