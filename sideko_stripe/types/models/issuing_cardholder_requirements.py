import pydantic
import typing
import typing_extensions


class IssuingCardholderRequirements(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disabled_reason: typing.Optional[
        typing_extensions.Literal[
            "listed", "rejected.listed", "requirements.past_due", "under_review"
        ]
    ] = pydantic.Field(alias="disabled_reason", default=None)
    """
    If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason.
    """
    past_due: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "company.tax_id",
                "individual.card_issuing.user_terms_acceptance.date",
                "individual.card_issuing.user_terms_acceptance.ip",
                "individual.dob.day",
                "individual.dob.month",
                "individual.dob.year",
                "individual.first_name",
                "individual.last_name",
                "individual.verification.document",
            ]
        ]
    ] = pydantic.Field(alias="past_due", default=None)
    """
    Array of fields that need to be collected in order to verify and re-enable the cardholder.
    """
