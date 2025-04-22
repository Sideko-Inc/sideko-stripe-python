import pydantic
import typing
import typing_extensions


class AccountCreateBodyDocumentsCompanyMinisterialDecree(typing_extensions.TypedDict):
    """
    AccountCreateBodyDocumentsCompanyMinisterialDecree
    """

    files: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountCreateBodyDocumentsCompanyMinisterialDecree(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyDocumentsCompanyMinisterialDecree handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
