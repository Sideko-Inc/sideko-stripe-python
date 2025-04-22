import pydantic
import typing
import typing_extensions

from .token_create_body_person_verification_additional_document import (
    TokenCreateBodyPersonVerificationAdditionalDocument,
    _SerializerTokenCreateBodyPersonVerificationAdditionalDocument,
)
from .token_create_body_person_verification_document import (
    TokenCreateBodyPersonVerificationDocument,
    _SerializerTokenCreateBodyPersonVerificationDocument,
)


class TokenCreateBodyPersonVerification(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonVerification
    """

    additional_document: typing_extensions.NotRequired[
        TokenCreateBodyPersonVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[TokenCreateBodyPersonVerificationDocument]


class _SerializerTokenCreateBodyPersonVerification(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerTokenCreateBodyPersonVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[_SerializerTokenCreateBodyPersonVerificationDocument] = (
        pydantic.Field(alias="document", default=None)
    )
