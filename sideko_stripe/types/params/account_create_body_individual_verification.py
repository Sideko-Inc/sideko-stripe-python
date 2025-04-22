import pydantic
import typing
import typing_extensions

from .account_create_body_individual_verification_additional_document import (
    AccountCreateBodyIndividualVerificationAdditionalDocument,
    _SerializerAccountCreateBodyIndividualVerificationAdditionalDocument,
)
from .account_create_body_individual_verification_document import (
    AccountCreateBodyIndividualVerificationDocument,
    _SerializerAccountCreateBodyIndividualVerificationDocument,
)


class AccountCreateBodyIndividualVerification(typing_extensions.TypedDict):
    """
    AccountCreateBodyIndividualVerification
    """

    additional_document: typing_extensions.NotRequired[
        AccountCreateBodyIndividualVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[
        AccountCreateBodyIndividualVerificationDocument
    ]


class _SerializerAccountCreateBodyIndividualVerification(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyIndividualVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountCreateBodyIndividualVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountCreateBodyIndividualVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
