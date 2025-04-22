import pydantic
import typing
import typing_extensions


class TokenCreateBodyPersonRelationship(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonRelationship
    """

    authorizer: typing_extensions.NotRequired[bool]

    director: typing_extensions.NotRequired[bool]

    executive: typing_extensions.NotRequired[bool]

    legal_guardian: typing_extensions.NotRequired[bool]

    owner: typing_extensions.NotRequired[bool]

    percent_ownership: typing_extensions.NotRequired[typing.Union[float, str]]

    representative: typing_extensions.NotRequired[bool]

    title: typing_extensions.NotRequired[str]


class _SerializerTokenCreateBodyPersonRelationship(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonRelationship handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authorizer: typing.Optional[bool] = pydantic.Field(alias="authorizer", default=None)
    director: typing.Optional[bool] = pydantic.Field(alias="director", default=None)
    executive: typing.Optional[bool] = pydantic.Field(alias="executive", default=None)
    legal_guardian: typing.Optional[bool] = pydantic.Field(
        alias="legal_guardian", default=None
    )
    owner: typing.Optional[bool] = pydantic.Field(alias="owner", default=None)
    percent_ownership: typing.Optional[typing.Union[float, str]] = pydantic.Field(
        alias="percent_ownership", default=None
    )
    representative: typing.Optional[bool] = pydantic.Field(
        alias="representative", default=None
    )
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
