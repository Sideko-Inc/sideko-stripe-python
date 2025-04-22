import pydantic
import typing
import typing_extensions

from .subscription_item_metadata import SubscriptionItemMetadata
from .tax_rate import TaxRate

if typing_extensions.TYPE_CHECKING:
    from .discount import Discount
    from .price import Price


class SubscriptionItem(pydantic.BaseModel):
    """
    Subscription items allow you to create customer subscriptions with more than
    one plan, making it easy to represent complex billing relationships.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    current_period_end: int = pydantic.Field(
        alias="current_period_end",
    )
    """
    The end time of this subscription item's current billing period.
    """
    current_period_start: int = pydantic.Field(
        alias="current_period_start",
    )
    """
    The start time of this subscription item's current billing period.
    """
    discounts: typing.List[typing.Union[str, "Discount"]] = pydantic.Field(
        alias="discounts",
    )
    """
    The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    metadata: SubscriptionItemMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["subscription_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: "Price" = pydantic.Field(
        alias="price",
    )
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.
    
    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.
    
    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The [quantity](https://stripe.com/docs/subscriptions/quantities) of the plan to which the customer should be subscribed.
    """
    subscription: str = pydantic.Field(
        alias="subscription",
    )
    """
    The `subscription` this `subscription_item` belongs to.
    """
    tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    """
    The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
    """
