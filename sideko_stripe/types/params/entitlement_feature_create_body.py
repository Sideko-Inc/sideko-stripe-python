import pydantic
import typing
import typing_extensions

from .entitlement_feature_create_body_metadata import (
    EntitlementFeatureCreateBodyMetadata,
    _SerializerEntitlementFeatureCreateBodyMetadata,
)


class EntitlementFeatureCreateBody(typing_extensions.TypedDict, total=False):
    """
    EntitlementFeatureCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    lookup_key: typing_extensions.Required[str]
    """
    A unique key you provide as your own system identifier. This may be up to 80 characters.
    """

    metadata: typing_extensions.NotRequired[EntitlementFeatureCreateBodyMetadata]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """

    name: typing_extensions.Required[str]
    """
    The feature's name, for your own purpose, not meant to be displayable to the customer.
    """


class _SerializerEntitlementFeatureCreateBody(pydantic.BaseModel):
    """
    Serializer for EntitlementFeatureCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    lookup_key: str = pydantic.Field(
        alias="lookup_key",
    )
    metadata: typing.Optional[_SerializerEntitlementFeatureCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
