import pydantic
import typing
import typing_extensions

from .issuing_cardholder_create_body_individual_card_issuing_user_terms_acceptance import (
    IssuingCardholderCreateBodyIndividualCardIssuingUserTermsAcceptance,
    _SerializerIssuingCardholderCreateBodyIndividualCardIssuingUserTermsAcceptance,
)


class IssuingCardholderCreateBodyIndividualCardIssuing(typing_extensions.TypedDict):
    """
    IssuingCardholderCreateBodyIndividualCardIssuing
    """

    user_terms_acceptance: typing_extensions.NotRequired[
        IssuingCardholderCreateBodyIndividualCardIssuingUserTermsAcceptance
    ]


class _SerializerIssuingCardholderCreateBodyIndividualCardIssuing(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyIndividualCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    user_terms_acceptance: typing.Optional[
        _SerializerIssuingCardholderCreateBodyIndividualCardIssuingUserTermsAcceptance
    ] = pydantic.Field(alias="user_terms_acceptance", default=None)
