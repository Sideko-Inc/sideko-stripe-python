import pydantic
import typing
import typing_extensions

from .issuing_cardholder_update_body_individual_card_issuing import (
    IssuingCardholderUpdateBodyIndividualCardIssuing,
    _SerializerIssuingCardholderUpdateBodyIndividualCardIssuing,
)
from .issuing_cardholder_update_body_individual_dob import (
    IssuingCardholderUpdateBodyIndividualDob,
    _SerializerIssuingCardholderUpdateBodyIndividualDob,
)
from .issuing_cardholder_update_body_individual_verification import (
    IssuingCardholderUpdateBodyIndividualVerification,
    _SerializerIssuingCardholderUpdateBodyIndividualVerification,
)


class IssuingCardholderUpdateBodyIndividual(typing_extensions.TypedDict):
    """
    Additional information about an `individual` cardholder.
    """

    card_issuing: typing_extensions.NotRequired[
        IssuingCardholderUpdateBodyIndividualCardIssuing
    ]

    dob: typing_extensions.NotRequired[IssuingCardholderUpdateBodyIndividualDob]

    first_name: typing_extensions.NotRequired[str]

    last_name: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[
        IssuingCardholderUpdateBodyIndividualVerification
    ]


class _SerializerIssuingCardholderUpdateBodyIndividual(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBodyIndividual handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_issuing: typing.Optional[
        _SerializerIssuingCardholderUpdateBodyIndividualCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    dob: typing.Optional[_SerializerIssuingCardholderUpdateBodyIndividualDob] = (
        pydantic.Field(alias="dob", default=None)
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    verification: typing.Optional[
        _SerializerIssuingCardholderUpdateBodyIndividualVerification
    ] = pydantic.Field(alias="verification", default=None)
