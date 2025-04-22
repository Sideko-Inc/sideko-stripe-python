import pydantic

from .portal_customer_update import PortalCustomerUpdate
from .portal_invoice_list import PortalInvoiceList
from .portal_payment_method_update import PortalPaymentMethodUpdate
from .portal_subscription_cancel import PortalSubscriptionCancel
from .portal_subscription_update import PortalSubscriptionUpdate


class PortalFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_update: PortalCustomerUpdate = pydantic.Field(
        alias="customer_update",
    )
    invoice_history: PortalInvoiceList = pydantic.Field(
        alias="invoice_history",
    )
    payment_method_update: PortalPaymentMethodUpdate = pydantic.Field(
        alias="payment_method_update",
    )
    subscription_cancel: PortalSubscriptionCancel = pydantic.Field(
        alias="subscription_cancel",
    )
    subscription_update: PortalSubscriptionUpdate = pydantic.Field(
        alias="subscription_update",
    )
