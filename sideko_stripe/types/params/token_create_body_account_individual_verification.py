import pydantic
import typing
import typing_extensions

from .token_create_body_account_individual_verification_additional_document import (
    TokenCreateBodyAccountIndividualVerificationAdditionalDocument,
    _SerializerTokenCreateBodyAccountIndividualVerificationAdditionalDocument,
)
from .token_create_body_account_individual_verification_document import (
    TokenCreateBodyAccountIndividualVerificationDocument,
    _SerializerTokenCreateBodyAccountIndividualVerificationDocument,
)


class TokenCreateBodyAccountIndividualVerification(typing_extensions.TypedDict):
    """
    TokenCreateBodyAccountIndividualVerification
    """

    additional_document: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualVerificationDocument
    ]


class _SerializerTokenCreateBodyAccountIndividualVerification(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyAccountIndividualVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
