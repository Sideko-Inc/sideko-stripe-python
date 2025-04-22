import pydantic
import typing
import typing_extensions


class AccountPersonCreateBodyDocumentsVisa(typing_extensions.TypedDict):
    """
    AccountPersonCreateBodyDocumentsVisa
    """

    files: typing_extensions.NotRequired[typing.List[typing.Union[str, str]]]


class _SerializerAccountPersonCreateBodyDocumentsVisa(pydantic.BaseModel):
    """
    Serializer for AccountPersonCreateBodyDocumentsVisa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[typing.Union[str, str]]] = pydantic.Field(
        alias="files", default=None
    )
