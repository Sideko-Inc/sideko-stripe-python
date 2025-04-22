import pydantic
import typing
import typing_extensions


class TokenCreateBodyPersonVerificationDocument(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonVerificationDocument
    """

    back: typing_extensions.NotRequired[str]

    front: typing_extensions.NotRequired[str]


class _SerializerTokenCreateBodyPersonVerificationDocument(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonVerificationDocument handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    back: typing.Optional[str] = pydantic.Field(alias="back", default=None)
    front: typing.Optional[str] = pydantic.Field(alias="front", default=None)
