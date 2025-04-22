import pydantic
import typing
import typing_extensions

from .deleted_price import DeletedPrice
from .subscription_schedule_configuration_item_metadata import (
    SubscriptionScheduleConfigurationItemMetadata,
)
from .tax_rate import TaxRate

if typing_extensions.TYPE_CHECKING:
    from .discounts_resource_stackable_discount import (
        DiscountsResourceStackableDiscount,
    )
    from .price import Price


class SubscriptionScheduleConfigurationItem(pydantic.BaseModel):
    """
    A phase item describes the price and quantity of a phase.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    discounts: typing.List["DiscountsResourceStackableDiscount"] = pydantic.Field(
        alias="discounts",
    )
    """
    The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
    """
    metadata: typing.Optional[SubscriptionScheduleConfigurationItemMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered.
    """
    price: typing.Union[str, "Price", DeletedPrice] = pydantic.Field(
        alias="price",
    )
    """
    ID of the price to which the customer should be subscribed.
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    Quantity of the plan to which the customer should be subscribed.
    """
    tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    """
    The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`.
    """
