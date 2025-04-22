import pydantic
import typing


class BillingBillResourceInvoiceItemParentsInvoiceItemSubscriptionParent(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription: str = pydantic.Field(
        alias="subscription",
    )
    """
    The subscription that generated this invoice item
    """
    subscription_item: typing.Optional[str] = pydantic.Field(
        alias="subscription_item", default=None
    )
    """
    The subscription item that generated this invoice item
    """
