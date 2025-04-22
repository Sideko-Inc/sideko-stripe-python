import pydantic
import typing
import typing_extensions

from .account_people_update_body_verification_additional_document import (
    AccountPeopleUpdateBodyVerificationAdditionalDocument,
    _SerializerAccountPeopleUpdateBodyVerificationAdditionalDocument,
)
from .account_people_update_body_verification_document import (
    AccountPeopleUpdateBodyVerificationDocument,
    _SerializerAccountPeopleUpdateBodyVerificationDocument,
)


class AccountPeopleUpdateBodyVerification(typing_extensions.TypedDict):
    """
    The person's verification status.
    """

    additional_document: typing_extensions.NotRequired[
        AccountPeopleUpdateBodyVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[AccountPeopleUpdateBodyVerificationDocument]


class _SerializerAccountPeopleUpdateBodyVerification(pydantic.BaseModel):
    """
    Serializer for AccountPeopleUpdateBodyVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountPeopleUpdateBodyVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountPeopleUpdateBodyVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
