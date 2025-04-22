import pydantic
import typing
import typing_extensions

from .tax_rate_create_body_metadata import (
    TaxRateCreateBodyMetadata,
    _SerializerTaxRateCreateBodyMetadata,
)


class TaxRateCreateBody(typing_extensions.TypedDict, total=False):
    """
    TaxRateCreateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
    """

    country: typing_extensions.NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
    """

    display_name: typing_extensions.Required[str]
    """
    The display name of the tax rate, which will be shown to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    inclusive: typing_extensions.Required[bool]
    """
    This specifies if the tax rate is inclusive or exclusive.
    """

    jurisdiction: typing_extensions.NotRequired[str]
    """
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
    """

    metadata: typing_extensions.NotRequired[TaxRateCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    percentage: typing_extensions.Required[float]
    """
    This represents the tax rate percent out of 100.
    """

    state: typing_extensions.NotRequired[str]
    """
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
    """

    tax_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "retail_delivery_fee",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ]
    """
    The high-level tax type, such as `vat` or `sales_tax`.
    """


class _SerializerTaxRateCreateBody(pydantic.BaseModel):
    """
    Serializer for TaxRateCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    inclusive: bool = pydantic.Field(
        alias="inclusive",
    )
    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    metadata: typing.Optional[_SerializerTaxRateCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    percentage: float = pydantic.Field(
        alias="percentage",
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    tax_type: typing.Optional[
        typing_extensions.Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "retail_delivery_fee",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ] = pydantic.Field(alias="tax_type", default=None)
