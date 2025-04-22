import pydantic
import typing
import typing_extensions

from .token_create_body_account_company_verification_document import (
    TokenCreateBodyAccountCompanyVerificationDocument,
    _SerializerTokenCreateBodyAccountCompanyVerificationDocument,
)


class TokenCreateBodyAccountCompanyVerification(typing_extensions.TypedDict):
    """
    TokenCreateBodyAccountCompanyVerification
    """

    document: typing_extensions.NotRequired[
        TokenCreateBodyAccountCompanyVerificationDocument
    ]


class _SerializerTokenCreateBodyAccountCompanyVerification(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyAccountCompanyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        _SerializerTokenCreateBodyAccountCompanyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
