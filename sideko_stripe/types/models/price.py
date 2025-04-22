import pydantic
import typing
import typing_extensions

from .custom_unit_amount import CustomUnitAmount
from .deleted_product import DeletedProduct
from .price_currency_options import PriceCurrencyOptions
from .price_metadata import PriceMetadata
from .price_tier import PriceTier
from .recurring import Recurring
from .transform_quantity import TransformQuantity

if typing_extensions.TYPE_CHECKING:
    from .product import Product


class Price(pydantic.BaseModel):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the price can be used for new purchases.
    """
    billing_scheme: typing_extensions.Literal["per_unit", "tiered"] = pydantic.Field(
        alias="billing_scheme",
    )
    """
    Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
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
    currency_options: typing.Optional[PriceCurrencyOptions] = pydantic.Field(
        alias="currency_options", default=None
    )
    """
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """
    custom_unit_amount: typing.Optional[CustomUnitAmount] = pydantic.Field(
        alias="custom_unit_amount", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: typing.Optional[str] = pydantic.Field(alias="lookup_key", default=None)
    """
    A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
    """
    metadata: PriceMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    """
    A brief description of the price, hidden from customers.
    """
    object: typing_extensions.Literal["price"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: typing.Union[str, "Product", DeletedProduct] = pydantic.Field(
        alias="product",
    )
    """
    The ID of the product this price is associated with.
    """
    recurring: typing.Optional[Recurring] = pydantic.Field(
        alias="recurring", default=None
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    tiers: typing.Optional[typing.List[PriceTier]] = pydantic.Field(
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
    transform_quantity: typing.Optional[TransformQuantity] = pydantic.Field(
        alias="transform_quantity", default=None
    )
    type_: typing_extensions.Literal["one_time", "recurring"] = pydantic.Field(
        alias="type",
    )
    """
    One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.
    """
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.
    """
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.
    """
