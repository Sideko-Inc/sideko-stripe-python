import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_parents_invoice_subscription_parent_metadata import (
    BillingBillResourceInvoicingParentsInvoiceSubscriptionParentMetadata,
)

if typing_extensions.TYPE_CHECKING:
    from .subscription import Subscription


class BillingBillResourceInvoicingParentsInvoiceSubscriptionParent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    metadata: typing.Optional[
        BillingBillResourceInvoicingParentsInvoiceSubscriptionParentMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) defined as subscription metadata when an invoice is created. Becomes an immutable snapshot of the subscription metadata at the time of invoice finalization.
     *Note: This attribute is populated only for invoices created on or after June 29, 2023.*
    """
    subscription: typing.Union[str, "Subscription"] = pydantic.Field(
        alias="subscription",
    )
    """
    The subscription that generated this invoice
    """
    subscription_proration_date: typing.Optional[int] = pydantic.Field(
        alias="subscription_proration_date", default=None
    )
    """
    Only set for upcoming invoices that preview prorations. The time used to calculate prorations.
    """
