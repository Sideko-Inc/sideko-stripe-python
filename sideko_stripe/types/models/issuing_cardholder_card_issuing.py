import pydantic
import typing

from .issuing_cardholder_user_terms_acceptance import (
    IssuingCardholderUserTermsAcceptance,
)


class IssuingCardholderCardIssuing(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_terms_acceptance: typing.Optional[IssuingCardholderUserTermsAcceptance] = (
        pydantic.Field(alias="user_terms_acceptance", default=None)
    )
