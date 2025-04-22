import pydantic
import typing
import typing_extensions


class IssuingTokenUpdateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingTokenUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    status: typing_extensions.Required[
        typing_extensions.Literal["active", "deleted", "suspended"]
    ]
    """
    Specifies which status the token should be updated to.
    """


class _SerializerIssuingTokenUpdateBody(pydantic.BaseModel):
    """
    Serializer for IssuingTokenUpdateBody handling case conversions
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
    status: typing_extensions.Literal["active", "deleted", "suspended"] = (
        pydantic.Field(
            alias="status",
        )
    )
