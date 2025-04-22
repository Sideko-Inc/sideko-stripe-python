import pydantic
import typing


class BillingBillResourceInvoicingParentsInvoiceSubscriptionParentMetadata(
    pydantic.BaseModel
):
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) defined as subscription metadata when an invoice is created. Becomes an immutable snapshot of the subscription metadata at the time of invoice finalization.
     *Note: This attribute is populated only for invoices created on or after June 29, 2023.*
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, str]
