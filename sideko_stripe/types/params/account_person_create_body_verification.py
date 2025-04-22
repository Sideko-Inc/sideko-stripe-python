import pydantic
import typing
import typing_extensions

from .account_person_create_body_verification_additional_document import (
    AccountPersonCreateBodyVerificationAdditionalDocument,
    _SerializerAccountPersonCreateBodyVerificationAdditionalDocument,
)
from .account_person_create_body_verification_document import (
    AccountPersonCreateBodyVerificationDocument,
    _SerializerAccountPersonCreateBodyVerificationDocument,
)


class AccountPersonCreateBodyVerification(typing_extensions.TypedDict):
    """
    The person's verification status.
    """

    additional_document: typing_extensions.NotRequired[
        AccountPersonCreateBodyVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[AccountPersonCreateBodyVerificationDocument]


class _SerializerAccountPersonCreateBodyVerification(pydantic.BaseModel):
    """
    Serializer for AccountPersonCreateBodyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountPersonCreateBodyVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountPersonCreateBodyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
