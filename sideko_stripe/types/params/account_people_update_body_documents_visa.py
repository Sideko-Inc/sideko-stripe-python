import pydantic
import typing
import typing_extensions


class AccountPeopleUpdateBodyDocumentsVisa(typing_extensions.TypedDict):
    """
    AccountPeopleUpdateBodyDocumentsVisa
    """

    files: typing_extensions.NotRequired[typing.List[typing.Union[str, str]]]


class _SerializerAccountPeopleUpdateBodyDocumentsVisa(pydantic.BaseModel):
    """
    Serializer for AccountPeopleUpdateBodyDocumentsVisa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[typing.Union[str, str]]] = pydantic.Field(
        alias="files", default=None
    )
