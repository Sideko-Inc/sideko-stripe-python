import pydantic
import typing
import typing_extensions


class AccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    """

    files: typing_extensions.NotRequired[typing.List[str]]


class _SerializerAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
