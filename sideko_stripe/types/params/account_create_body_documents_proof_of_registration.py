import pydantic
import typing
import typing_extensions


class AccountCreateBodyDocumentsProofOfRegistration(typing_extensions.TypedDict):
    """
    AccountCreateBodyDocumentsProofOfRegistration
    """

    files: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountCreateBodyDocumentsProofOfRegistration(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyDocumentsProofOfRegistration handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
