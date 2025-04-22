import pydantic
import typing
import typing_extensions


class RadarValueListItemCreateBody(typing_extensions.TypedDict, total=False):
    """
    RadarValueListItemCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    value: typing_extensions.Required[str]
    """
    The value of the item (whose type must match the type of the parent value list).
    """

    value_list: typing_extensions.Required[str]
    """
    The identifier of the value list which the created item will be added to.
    """


class _SerializerRadarValueListItemCreateBody(pydantic.BaseModel):
    """
    Serializer for RadarValueListItemCreateBody handling case conversions
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
    value: str = pydantic.Field(
        alias="value",
    )
    value_list: str = pydantic.Field(
        alias="value_list",
    )
