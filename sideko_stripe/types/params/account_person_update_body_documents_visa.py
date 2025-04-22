import pydantic
import typing
import typing_extensions


class AccountPersonUpdateBodyDocumentsVisa(typing_extensions.TypedDict):
    """
    AccountPersonUpdateBodyDocumentsVisa
    """

    files: typing_extensions.NotRequired[typing.List[typing.Union[str, str]]]


class _SerializerAccountPersonUpdateBodyDocumentsVisa(pydantic.BaseModel):
    """
    Serializer for AccountPersonUpdateBodyDocumentsVisa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[typing.Union[str, str]]] = pydantic.Field(
        alias="files", default=None
    )
