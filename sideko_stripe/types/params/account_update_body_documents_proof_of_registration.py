import pydantic
import typing
import typing_extensions


class AccountUpdateBodyDocumentsProofOfRegistration(typing_extensions.TypedDict):
    """
    AccountUpdateBodyDocumentsProofOfRegistration
    """

    files: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountUpdateBodyDocumentsProofOfRegistration(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyDocumentsProofOfRegistration handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
