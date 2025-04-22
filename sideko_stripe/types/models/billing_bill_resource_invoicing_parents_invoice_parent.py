import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_parents_invoice_quote_parent import (
    BillingBillResourceInvoicingParentsInvoiceQuoteParent,
)

if typing_extensions.TYPE_CHECKING:
    from .billing_bill_resource_invoicing_parents_invoice_subscription_parent import (
        BillingBillResourceInvoicingParentsInvoiceSubscriptionParent,
    )


class BillingBillResourceInvoicingParentsInvoiceParent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    quote_details: typing.Optional[
        BillingBillResourceInvoicingParentsInvoiceQuoteParent
    ] = pydantic.Field(alias="quote_details", default=None)
    subscription_details: typing.Optional[
        "BillingBillResourceInvoicingParentsInvoiceSubscriptionParent"
    ] = pydantic.Field(alias="subscription_details", default=None)
    type_: typing_extensions.Literal["quote_details", "subscription_details"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of parent that generated this invoice
    """
