import pydantic
import typing
import typing_extensions

from .account_update_body_individual_verification_additional_document import (
    AccountUpdateBodyIndividualVerificationAdditionalDocument,
    _SerializerAccountUpdateBodyIndividualVerificationAdditionalDocument,
)
from .account_update_body_individual_verification_document import (
    AccountUpdateBodyIndividualVerificationDocument,
    _SerializerAccountUpdateBodyIndividualVerificationDocument,
)


class AccountUpdateBodyIndividualVerification(typing_extensions.TypedDict):
    """
    AccountUpdateBodyIndividualVerification
    """

    additional_document: typing_extensions.NotRequired[
        AccountUpdateBodyIndividualVerificationAdditionalDocument
    ]

    document: typing_extensions.NotRequired[
        AccountUpdateBodyIndividualVerificationDocument
    ]


class _SerializerAccountUpdateBodyIndividualVerification(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyIndividualVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_document: typing.Optional[
        _SerializerAccountUpdateBodyIndividualVerificationAdditionalDocument
    ] = pydantic.Field(alias="additional_document", default=None)
    document: typing.Optional[
        _SerializerAccountUpdateBodyIndividualVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
