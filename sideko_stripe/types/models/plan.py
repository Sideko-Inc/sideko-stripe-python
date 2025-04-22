import pydantic
import typing
import typing_extensions

from .deleted_product import DeletedProduct
from .plan_metadata import PlanMetadata
from .plan_tier import PlanTier
from .transform_usage import TransformUsage

if typing_extensions.TYPE_CHECKING:
    from .product import Product


class Plan(pydantic.BaseModel):
    """
    You can now model subscriptions more flexibly using the [Prices API](https://stripe.com/docs/api#prices). It replaces the Plans API and is backwards compatible to simplify your migration.

    Plans define the base price, currency, and billing cycle for recurring purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has plans for $10/month, $100/year, €9/month, and €90/year.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription) and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the plan can be used for new purchases.
    """
    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.
    """
    amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="amount_decimal", default=None
    )
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.
    """
    billing_scheme: typing_extensions.Literal["per_unit", "tiered"] = pydantic.Field(
        alias="billing_scheme",
    )
    """
    Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    interval: typing_extensions.Literal["day", "month", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    """
    The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.
    """
    interval_count: int = pydantic.Field(
        alias="interval_count",
    )
    """
    The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[PlanMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    meter: typing.Optional[str] = pydantic.Field(alias="meter", default=None)
    """
    The meter tracking the usage of a metered price
    """
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    """
    A brief description of the plan, hidden from customers.
    """
    object: typing_extensions.Literal["plan"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: typing.Optional[typing.Union[str, "Product", DeletedProduct]] = (
        pydantic.Field(alias="product", default=None)
    )
    """
    The product whose pricing this plan determines.
    """
    tiers: typing.Optional[typing.List[PlanTier]] = pydantic.Field(
        alias="tiers", default=None
    )
    """
    Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
    """
    tiers_mode: typing.Optional[typing_extensions.Literal["graduated", "volume"]] = (
        pydantic.Field(alias="tiers_mode", default=None)
    )
    """
    Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
    """
    transform_usage: typing.Optional[TransformUsage] = pydantic.Field(
        alias="transform_usage", default=None
    )
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    """
    Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
    """
    usage_type: typing_extensions.Literal["licensed", "metered"] = pydantic.Field(
        alias="usage_type",
    )
    """
    Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
    """
