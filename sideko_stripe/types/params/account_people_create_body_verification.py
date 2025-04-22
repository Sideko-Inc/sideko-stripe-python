import pydantic
import typing
import typing_extensions

from .account_people_create_body_verification_additional_document import (
    AccountPeopleCreateBodyVerificationAdditionalDocument,
    _SerializerAccountPeopleCreateBodyVerificationAdditionalDocument,
)
from .account_people_create_body_verification_document import (
    AccountPeopleCreateBodyVerificationDocument,
    _SerializerAccountPeopleCreateBodyVerificationDocument,
)


class AccountPeopleCreateBodyVerification(typing_extensions.TypedDict):
    """
    The person's verification status.
    """

    additional_document: typing_extensions.NotRequired[
        AccountPeopleCreateBodyVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[AccountPeopleCreateBodyVerificationDocument]


class _SerializerAccountPeopleCreateBodyVerification(pydantic.BaseModel):
    """
    Serializer for AccountPeopleCreateBodyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountPeopleCreateBodyVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountPeopleCreateBodyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
