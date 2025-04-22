import pydantic
import typing
import typing_extensions

from .climate_order_create_body_beneficiary import (
    ClimateOrderCreateBodyBeneficiary,
    _SerializerClimateOrderCreateBodyBeneficiary,
)
from .climate_order_create_body_metadata import (
    ClimateOrderCreateBodyMetadata,
    _SerializerClimateOrderCreateBodyMetadata,
)


class ClimateOrderCreateBody(typing_extensions.TypedDict, total=False):
    """
    ClimateOrderCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Requested amount of carbon removal units. Either this or `metric_tons` must be specified.
    """

    beneficiary: typing_extensions.NotRequired[ClimateOrderCreateBodyBeneficiary]
    """
    Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[ClimateOrderCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    metric_tons: typing_extensions.NotRequired[str]
    """
    Requested number of tons for the order. Either this or `amount` must be specified.
    """

    product: typing_extensions.Required[str]
    """
    Unique identifier of the Climate product.
    """


class _SerializerClimateOrderCreateBody(pydantic.BaseModel):
    """
    Serializer for ClimateOrderCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    beneficiary: typing.Optional[_SerializerClimateOrderCreateBodyBeneficiary] = (
        pydantic.Field(alias="beneficiary", default=None)
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerClimateOrderCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    metric_tons: typing.Optional[str] = pydantic.Field(
        alias="metric_tons", default=None
    )
    product: str = pydantic.Field(
        alias="product",
    )
