import pydantic
import typing
import typing_extensions

from .issuing_cardholder_create_body_individual_verification_document import (
    IssuingCardholderCreateBodyIndividualVerificationDocument,
    _SerializerIssuingCardholderCreateBodyIndividualVerificationDocument,
)


class IssuingCardholderCreateBodyIndividualVerification(typing_extensions.TypedDict):
    """
    IssuingCardholderCreateBodyIndividualVerification
    """

    document: typing_extensions.NotRequired[
        IssuingCardholderCreateBodyIndividualVerificationDocument
    ]


class _SerializerIssuingCardholderCreateBodyIndividualVerification(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyIndividualVerification handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        _SerializerIssuingCardholderCreateBodyIndividualVerificationDocument
    ] = pydantic.Field(alias="document", default=None)
