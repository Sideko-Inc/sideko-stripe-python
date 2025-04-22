import pydantic
import typing
import typing_extensions

from .issuing_cardholder_create_body_individual_card_issuing import (
    IssuingCardholderCreateBodyIndividualCardIssuing,
    _SerializerIssuingCardholderCreateBodyIndividualCardIssuing,
)
from .issuing_cardholder_create_body_individual_dob import (
    IssuingCardholderCreateBodyIndividualDob,
    _SerializerIssuingCardholderCreateBodyIndividualDob,
)
from .issuing_cardholder_create_body_individual_verification import (
    IssuingCardholderCreateBodyIndividualVerification,
    _SerializerIssuingCardholderCreateBodyIndividualVerification,
)


class IssuingCardholderCreateBodyIndividual(typing_extensions.TypedDict):
    """
    Additional information about an `individual` cardholder.
    """

    card_issuing: typing_extensions.NotRequired[
        IssuingCardholderCreateBodyIndividualCardIssuing
    ]

    dob: typing_extensions.NotRequired[IssuingCardholderCreateBodyIndividualDob]

    first_name: typing_extensions.NotRequired[str]

    last_name: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[
        IssuingCardholderCreateBodyIndividualVerification
    ]


class _SerializerIssuingCardholderCreateBodyIndividual(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyIndividual handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_issuing: typing.Optional[
        _SerializerIssuingCardholderCreateBodyIndividualCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    dob: typing.Optional[_SerializerIssuingCardholderCreateBodyIndividualDob] = (
        pydantic.Field(alias="dob", default=None)
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    verification: typing.Optional[
        _SerializerIssuingCardholderCreateBodyIndividualVerification
    ] = pydantic.Field(alias="verification", default=None)
