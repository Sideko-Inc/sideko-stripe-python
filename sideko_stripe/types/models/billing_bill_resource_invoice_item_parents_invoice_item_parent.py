import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoice_item_parents_invoice_item_subscription_parent import (
    BillingBillResourceInvoiceItemParentsInvoiceItemSubscriptionParent,
)


class BillingBillResourceInvoiceItemParentsInvoiceItemParent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription_details: typing.Optional[
        BillingBillResourceInvoiceItemParentsInvoiceItemSubscriptionParent
    ] = pydantic.Field(alias="subscription_details", default=None)
    type_: typing_extensions.Literal["subscription_details"] = pydantic.Field(
        alias="type",
    )
    """
    The type of parent that generated this invoice item
    """
