import pydantic
import typing
import typing_extensions

from .issuing_cardholder_update_body_individual_card_issuing_user_terms_acceptance import (
    IssuingCardholderUpdateBodyIndividualCardIssuingUserTermsAcceptance,
    _SerializerIssuingCardholderUpdateBodyIndividualCardIssuingUserTermsAcceptance,
)


class IssuingCardholderUpdateBodyIndividualCardIssuing(typing_extensions.TypedDict):
    """
    IssuingCardholderUpdateBodyIndividualCardIssuing
    """

    user_terms_acceptance: typing_extensions.NotRequired[
        IssuingCardholderUpdateBodyIndividualCardIssuingUserTermsAcceptance
    ]


class _SerializerIssuingCardholderUpdateBodyIndividualCardIssuing(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBodyIndividualCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    user_terms_acceptance: typing.Optional[
        _SerializerIssuingCardholderUpdateBodyIndividualCardIssuingUserTermsAcceptance
    ] = pydantic.Field(alias="user_terms_acceptance", default=None)
