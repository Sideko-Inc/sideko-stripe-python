import pydantic
import typing
import typing_extensions


class TokenCreateBodyPersonDocumentsVisa(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonDocumentsVisa
    """

    files: typing_extensions.NotRequired[typing.List[typing.Union[str, str]]]


class _SerializerTokenCreateBodyPersonDocumentsVisa(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonDocumentsVisa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[typing.Union[str, str]]] = pydantic.Field(
        alias="files", default=None
    )
