import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .payment_links_resource_invoice_settings import (
        PaymentLinksResourceInvoiceSettings,
    )


class PaymentLinksResourceInvoiceCreation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Enable creating an invoice on successful payment.
    """
    invoice_data: typing.Optional["PaymentLinksResourceInvoiceSettings"] = (
        pydantic.Field(alias="invoice_data", default=None)
    )
