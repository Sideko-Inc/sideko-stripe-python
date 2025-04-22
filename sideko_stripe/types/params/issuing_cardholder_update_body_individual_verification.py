import pydantic
import typing
import typing_extensions

from .issuing_cardholder_update_body_individual_verification_document import (
    IssuingCardholderUpdateBodyIndividualVerificationDocument,
    _SerializerIssuingCardholderUpdateBodyIndividualVerificationDocument,
)


class IssuingCardholderUpdateBodyIndividualVerification(typing_extensions.TypedDict):
    """
    IssuingCardholderUpdateBodyIndividualVerification
    """

    document: typing_extensions.NotRequired[
        IssuingCardholderUpdateBodyIndividualVerificationDocument
    ]


class _SerializerIssuingCardholderUpdateBodyIndividualVerification(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBodyIndividualVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        _SerializerIssuingCardholderUpdateBodyIndividualVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
