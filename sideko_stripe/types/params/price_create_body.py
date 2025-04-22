import pydantic
import typing
import typing_extensions

from .price_create_body_currency_options import (
    PriceCreateBodyCurrencyOptions,
    _SerializerPriceCreateBodyCurrencyOptions,
)
from .price_create_body_custom_unit_amount import (
    PriceCreateBodyCustomUnitAmount,
    _SerializerPriceCreateBodyCustomUnitAmount,
)
from .price_create_body_metadata import (
    PriceCreateBodyMetadata,
    _SerializerPriceCreateBodyMetadata,
)
from .price_create_body_product_data import (
    PriceCreateBodyProductData,
    _SerializerPriceCreateBodyProductData,
)
from .price_create_body_recurring import (
    PriceCreateBodyRecurring,
    _SerializerPriceCreateBodyRecurring,
)
from .price_create_body_tiers_item import (
    PriceCreateBodyTiersItem,
    _SerializerPriceCreateBodyTiersItem,
)
from .price_create_body_transform_quantity import (
    PriceCreateBodyTransformQuantity,
    _SerializerPriceCreateBodyTransformQuantity,
)


class PriceCreateBody(typing_extensions.TypedDict, total=False):
    """
    PriceCreateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the price can be used for new purchases. Defaults to `true`.
    """

    billing_scheme: typing_extensions.NotRequired[
        typing_extensions.Literal["per_unit", "tiered"]
    ]
    """
    Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    currency_options: typing_extensions.NotRequired[PriceCreateBodyCurrencyOptions]
    """
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    custom_unit_amount: typing_extensions.NotRequired[PriceCreateBodyCustomUnitAmount]
    """
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    lookup_key: typing_extensions.NotRequired[str]
    """
    A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
    """

    metadata: typing_extensions.NotRequired[PriceCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nickname: typing_extensions.NotRequired[str]
    """
    A brief description of the price, hidden from customers.
    """

    product: typing_extensions.NotRequired[str]
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
    """

    product_data: typing_extensions.NotRequired[PriceCreateBodyProductData]
    """
    These fields can be used to create a new product that this price will belong to.
    """

    recurring: typing_extensions.NotRequired[PriceCreateBodyRecurring]
    """
    The recurring components of a price such as `interval` and `usage_type`.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """

    tiers: typing_extensions.NotRequired[typing.List[PriceCreateBodyTiersItem]]
    """
    Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
    """

    tiers_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["graduated", "volume"]
    ]
    """
    Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
    """

    transfer_lookup_key: typing_extensions.NotRequired[bool]
    """
    If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.
    """

    transform_quantity: typing_extensions.NotRequired[PriceCreateBodyTransformQuantity]
    """
    Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    """

    unit_amount: typing_extensions.NotRequired[int]
    """
    A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`.
    """

    unit_amount_decimal: typing_extensions.NotRequired[str]
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
    """


class _SerializerPriceCreateBody(pydantic.BaseModel):
    """
    Serializer for PriceCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    billing_scheme: typing.Optional[typing_extensions.Literal["per_unit", "tiered"]] = (
        pydantic.Field(alias="billing_scheme", default=None)
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    currency_options: typing.Optional[_SerializerPriceCreateBodyCurrencyOptions] = (
        pydantic.Field(alias="currency_options", default=None)
    )
    custom_unit_amount: typing.Optional[_SerializerPriceCreateBodyCustomUnitAmount] = (
        pydantic.Field(alias="custom_unit_amount", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    lookup_key: typing.Optional[str] = pydantic.Field(alias="lookup_key", default=None)
    metadata: typing.Optional[_SerializerPriceCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    product_data: typing.Optional[_SerializerPriceCreateBodyProductData] = (
        pydantic.Field(alias="product_data", default=None)
    )
    recurring: typing.Optional[_SerializerPriceCreateBodyRecurring] = pydantic.Field(
        alias="recurring", default=None
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tiers: typing.Optional[typing.List[_SerializerPriceCreateBodyTiersItem]] = (
        pydantic.Field(alias="tiers", default=None)
    )
    tiers_mode: typing.Optional[typing_extensions.Literal["graduated", "volume"]] = (
        pydantic.Field(alias="tiers_mode", default=None)
    )
    transfer_lookup_key: typing.Optional[bool] = pydantic.Field(
        alias="transfer_lookup_key", default=None
    )
    transform_quantity: typing.Optional[_SerializerPriceCreateBodyTransformQuantity] = (
        pydantic.Field(alias="transform_quantity", default=None)
    )
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
