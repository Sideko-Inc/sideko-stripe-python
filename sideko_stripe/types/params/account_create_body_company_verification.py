import pydantic
import typing
import typing_extensions

from .account_create_body_company_verification_document import (
    AccountCreateBodyCompanyVerificationDocument,
    _SerializerAccountCreateBodyCompanyVerificationDocument,
)


class AccountCreateBodyCompanyVerification(typing_extensions.TypedDict):
    """
    AccountCreateBodyCompanyVerification
    """

    document: typing_extensions.NotRequired[
        AccountCreateBodyCompanyVerificationDocument
    ]


class _SerializerAccountCreateBodyCompanyVerification(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCompanyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        _SerializerAccountCreateBodyCompanyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
