import pydantic
import typing
import typing_extensions

from .promotion_code_create_body_metadata import (
    PromotionCodeCreateBodyMetadata,
    _SerializerPromotionCodeCreateBodyMetadata,
)
from .promotion_code_create_body_restrictions import (
    PromotionCodeCreateBodyRestrictions,
    _SerializerPromotionCodeCreateBodyRestrictions,
)


class PromotionCodeCreateBody(typing_extensions.TypedDict, total=False):
    """
    PromotionCodeCreateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the promotion code is currently active.
    """

    code: typing_extensions.NotRequired[str]
    """
    The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).
    
    If left blank, we will generate one automatically.
    """

    coupon: typing_extensions.Required[str]
    """
    The coupon for this promotion code.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`.
    """

    max_redemptions: typing_extensions.NotRequired[int]
    """
    A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`.
    """

    metadata: typing_extensions.NotRequired[PromotionCodeCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    restrictions: typing_extensions.NotRequired[PromotionCodeCreateBodyRestrictions]
    """
    Settings that restrict the redemption of the promotion code.
    """


class _SerializerPromotionCodeCreateBody(pydantic.BaseModel):
    """
    Serializer for PromotionCodeCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    code: typing.Optional[str] = pydantic.Field(alias="code", default=None)
    coupon: str = pydantic.Field(
        alias="coupon",
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    max_redemptions: typing.Optional[int] = pydantic.Field(
        alias="max_redemptions", default=None
    )
    metadata: typing.Optional[_SerializerPromotionCodeCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    restrictions: typing.Optional[_SerializerPromotionCodeCreateBodyRestrictions] = (
        pydantic.Field(alias="restrictions", default=None)
    )
