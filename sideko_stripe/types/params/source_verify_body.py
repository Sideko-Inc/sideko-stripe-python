import pydantic
import typing
import typing_extensions


class SourceVerifyBody(typing_extensions.TypedDict, total=False):
    """
    SourceVerifyBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    values: typing_extensions.Required[typing.List[str]]
    """
    The values needed to verify the source.
    """


class _SerializerSourceVerifyBody(pydantic.BaseModel):
    """
    Serializer for SourceVerifyBody handling case conversions
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
    values: typing.List[str] = pydantic.Field(
        alias="values",
    )
