import pydantic
import typing
import typing_extensions


class TokenCreateBodyPii(typing_extensions.TypedDict):
    """
    The PII this token represents.
    """

    id_number: typing_extensions.NotRequired[str]


class _SerializerTokenCreateBodyPii(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPii handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id_number: typing.Optional[str] = pydantic.Field(alias="id_number", default=None)
