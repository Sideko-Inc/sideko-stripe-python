import pydantic
import typing
import typing_extensions


class IssuingCardGooglePay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    eligible: bool = pydantic.Field(
        alias="eligible",
    )
    """
    Google Pay Eligibility
    """
    ineligible_reason: typing.Optional[
        typing_extensions.Literal[
            "missing_agreement", "missing_cardholder_contact", "unsupported_region"
        ]
    ] = pydantic.Field(alias="ineligible_reason", default=None)
    """
    Reason the card is ineligible for Google Pay
    """
