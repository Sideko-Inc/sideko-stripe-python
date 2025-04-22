import pydantic
import typing
import typing_extensions

from .account_update_body_company_verification_document import (
    AccountUpdateBodyCompanyVerificationDocument,
    _SerializerAccountUpdateBodyCompanyVerificationDocument,
)


class AccountUpdateBodyCompanyVerification(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCompanyVerification
    """

    document: typing_extensions.NotRequired[
        AccountUpdateBodyCompanyVerificationDocument
    ]


class _SerializerAccountUpdateBodyCompanyVerification(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCompanyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        _SerializerAccountUpdateBodyCompanyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
