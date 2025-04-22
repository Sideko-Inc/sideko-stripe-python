import pydantic
import typing
import typing_extensions


class AccountPeopleUpdateBodyDocumentsPassport(typing_extensions.TypedDict):
    """
    AccountPeopleUpdateBodyDocumentsPassport
    """

    files: typing_extensions.NotRequired[typing.List[typing.Union[str, str]]]


class _SerializerAccountPeopleUpdateBodyDocumentsPassport(pydantic.BaseModel):
    """
    Serializer for AccountPeopleUpdateBodyDocumentsPassport handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[typing.Union[str, str]]] = pydantic.Field(
        alias="files", default=None
    )
