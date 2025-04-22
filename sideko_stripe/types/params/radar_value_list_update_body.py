import pydantic
import typing
import typing_extensions

from .radar_value_list_update_body_metadata import (
    RadarValueListUpdateBodyMetadata,
    _SerializerRadarValueListUpdateBodyMetadata,
)


class RadarValueListUpdateBody(typing_extensions.TypedDict, total=False):
    """
    RadarValueListUpdateBody
    """

    alias: typing_extensions.NotRequired[str]
    """
    The name of the value list for use in rules.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[RadarValueListUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    The human-readable name of the value list.
    """


class _SerializerRadarValueListUpdateBody(pydantic.BaseModel):
    """
    Serializer for RadarValueListUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    alias: typing.Optional[str] = pydantic.Field(alias="alias", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerRadarValueListUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
