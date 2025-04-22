import pydantic
import typing
import typing_extensions


class AccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification(
    typing_extensions.TypedDict
):
    """
    AccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    """

    files: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification(
    pydantic.BaseModel
):
    """
    Serializer for AccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
