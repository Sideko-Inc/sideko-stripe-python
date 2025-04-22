import pydantic
import typing
import typing_extensions

from .entitlement_feature_update_body_metadata_obj0 import (
    EntitlementFeatureUpdateBodyMetadataObj0,
    _SerializerEntitlementFeatureUpdateBodyMetadataObj0,
)


class EntitlementFeatureUpdateBody(typing_extensions.TypedDict, total=False):
    """
    EntitlementFeatureUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Inactive features cannot be attached to new products and will not be returned from the features list endpoint.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[EntitlementFeatureUpdateBodyMetadataObj0, str]
    ]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """

    name: typing_extensions.NotRequired[str]
    """
    The feature's name, for your own purpose, not meant to be displayable to the customer.
    """


class _SerializerEntitlementFeatureUpdateBody(pydantic.BaseModel):
    """
    Serializer for EntitlementFeatureUpdateBody handling case conversions
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
        typing.Union[_SerializerEntitlementFeatureUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
