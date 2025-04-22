import pydantic
import typing
import typing_extensions

from .issuing_cardholder_card_issuing import IssuingCardholderCardIssuing
from .issuing_cardholder_individual_dob import IssuingCardholderIndividualDob

if typing_extensions.TYPE_CHECKING:
    from .issuing_cardholder_verification import IssuingCardholderVerification


class IssuingCardholderIndividual(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_issuing: typing.Optional[IssuingCardholderCardIssuing] = pydantic.Field(
        alias="card_issuing", default=None
    )
    dob: typing.Optional[IssuingCardholderIndividualDob] = pydantic.Field(
        alias="dob", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    The last name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.
    """
    verification: typing.Optional["IssuingCardholderVerification"] = pydantic.Field(
        alias="verification", default=None
    )
