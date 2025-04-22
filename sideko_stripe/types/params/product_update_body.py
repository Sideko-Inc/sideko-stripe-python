import pydantic
import typing
import typing_extensions

from .product_update_body_marketing_features_arr0_item import (
    ProductUpdateBodyMarketingFeaturesArr0Item,
    _SerializerProductUpdateBodyMarketingFeaturesArr0Item,
)
from .product_update_body_metadata_obj0 import (
    ProductUpdateBodyMetadataObj0,
    _SerializerProductUpdateBodyMetadataObj0,
)
from .product_update_body_package_dimensions_obj0 import (
    ProductUpdateBodyPackageDimensionsObj0,
    _SerializerProductUpdateBodyPackageDimensionsObj0,
)


class ProductUpdateBody(typing_extensions.TypedDict, total=False):
    """
    ProductUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the product is available for purchase.
    """

    default_price: typing_extensions.NotRequired[str]
    """
    The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product.
    """

    description: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    images: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    """

    marketing_features: typing_extensions.NotRequired[
        typing.Union[typing.List[ProductUpdateBodyMarketingFeaturesArr0Item], str]
    ]
    """
    A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ProductUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    The product's name, meant to be displayable to the customer.
    """

    package_dimensions: typing_extensions.NotRequired[
        typing.Union[ProductUpdateBodyPackageDimensionsObj0, str]
    ]
    """
    The dimensions of this product for shipping purposes.
    """

    shippable: typing_extensions.NotRequired[bool]
    """
    Whether this product is shipped (i.e., physical goods).
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.
    
    This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
     It must contain at least one letter. May only be set if `type=service`. Only used for subscription payments.
    """

    tax_code: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    """

    unit_label: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`.
    """

    url: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A URL of a publicly-accessible webpage for this product.
    """


class _SerializerProductUpdateBody(pydantic.BaseModel):
    """
    Serializer for ProductUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    default_price: typing.Optional[str] = pydantic.Field(
        alias="default_price", default=None
    )
    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    images: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="images", default=None
    )
    marketing_features: typing.Optional[
        typing.Union[
            typing.List[_SerializerProductUpdateBodyMarketingFeaturesArr0Item], str
        ]
    ] = pydantic.Field(alias="marketing_features", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerProductUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    package_dimensions: typing.Optional[
        typing.Union[_SerializerProductUpdateBodyPackageDimensionsObj0, str]
    ] = pydantic.Field(alias="package_dimensions", default=None)
    shippable: typing.Optional[bool] = pydantic.Field(alias="shippable", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    tax_code: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="tax_code", default=None
    )
    unit_label: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="unit_label", default=None
    )
    url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="url", default=None
    )
