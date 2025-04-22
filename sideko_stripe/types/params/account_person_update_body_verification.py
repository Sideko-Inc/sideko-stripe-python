import pydantic
import typing
import typing_extensions

from .account_person_update_body_verification_additional_document import (
    AccountPersonUpdateBodyVerificationAdditionalDocument,
    _SerializerAccountPersonUpdateBodyVerificationAdditionalDocument,
)
from .account_person_update_body_verification_document import (
    AccountPersonUpdateBodyVerificationDocument,
    _SerializerAccountPersonUpdateBodyVerificationDocument,
)


class AccountPersonUpdateBodyVerification(typing_extensions.TypedDict):
    """
    The person's verification status.
    """

    additional_document: typing_extensions.NotRequired[
        AccountPersonUpdateBodyVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[AccountPersonUpdateBodyVerificationDocument]


class _SerializerAccountPersonUpdateBodyVerification(pydantic.BaseModel):
    """
    Serializer for AccountPersonUpdateBodyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountPersonUpdateBodyVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountPersonUpdateBodyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
