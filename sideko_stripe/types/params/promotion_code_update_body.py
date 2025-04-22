import pydantic
import typing
import typing_extensions

from .promotion_code_update_body_metadata_obj0 import (
    PromotionCodeUpdateBodyMetadataObj0,
    _SerializerPromotionCodeUpdateBodyMetadataObj0,
)
from .promotion_code_update_body_restrictions import (
    PromotionCodeUpdateBodyRestrictions,
    _SerializerPromotionCodeUpdateBodyRestrictions,
)


class PromotionCodeUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PromotionCodeUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PromotionCodeUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    restrictions: typing_extensions.NotRequired[PromotionCodeUpdateBodyRestrictions]
    """
    Settings that restrict the redemption of the promotion code.
    """


class _SerializerPromotionCodeUpdateBody(pydantic.BaseModel):
    """
    Serializer for PromotionCodeUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPromotionCodeUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    restrictions: typing.Optional[_SerializerPromotionCodeUpdateBodyRestrictions] = (
        pydantic.Field(alias="restrictions", default=None)
    )
