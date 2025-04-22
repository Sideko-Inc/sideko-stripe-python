import pydantic
import typing
import typing_extensions

from .package_dimensions import PackageDimensions
from .product_marketing_feature import ProductMarketingFeature
from .product_metadata import ProductMetadata
from .tax_code import TaxCode

if typing_extensions.TYPE_CHECKING:
    from .price import Price


class Product(pydantic.BaseModel):
    """
    Products describe the specific goods or services you offer to your customers.
    For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
    They can be used in conjunction with [Prices](https://stripe.com/docs/api#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription),
    [share a Payment Link](https://stripe.com/docs/payment-links),
    [accept payments with Checkout](https://stripe.com/docs/payments/accept-a-payment#create-product-prices-upfront),
    and more about [Products and Prices](https://stripe.com/docs/products-prices/overview)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the product is currently available for purchase.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    default_price: typing.Optional[typing.Union[str, "Price"]] = pydantic.Field(
        alias="default_price", default=None
    )
    """
    The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    images: typing.List[str] = pydantic.Field(
        alias="images",
    )
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    marketing_features: typing.List[ProductMarketingFeature] = pydantic.Field(
        alias="marketing_features",
    )
    """
    A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
    """
    metadata: ProductMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The product's name, meant to be displayable to the customer.
    """
    object: typing_extensions.Literal["product"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    package_dimensions: typing.Optional[PackageDimensions] = pydantic.Field(
        alias="package_dimensions", default=None
    )
    shippable: typing.Optional[bool] = pydantic.Field(alias="shippable", default=None)
    """
    Whether this product is shipped (i.e., physical goods).
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only used for subscription payments.
    """
    tax_code: typing.Optional[typing.Union[str, TaxCode]] = pydantic.Field(
        alias="tax_code", default=None
    )
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    """
    unit_label: typing.Optional[str] = pydantic.Field(alias="unit_label", default=None)
    """
    A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
    """
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    A URL of a publicly-accessible webpage for this product.
    """
