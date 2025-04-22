import pydantic
import typing
import typing_extensions


class DisputeEnhancedEligibilityVisaCompellingEvidence3(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    required_actions: typing.List[
        typing_extensions.Literal[
            "missing_customer_identifiers",
            "missing_disputed_transaction_description",
            "missing_merchandise_or_services",
            "missing_prior_undisputed_transaction_description",
            "missing_prior_undisputed_transactions",
        ]
    ] = pydantic.Field(
        alias="required_actions",
    )
    """
    List of actions required to qualify dispute for Visa Compelling Evidence 3.0 evidence submission.
    """
    status: typing_extensions.Literal[
        "not_qualified", "qualified", "requires_action"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Visa Compelling Evidence 3.0 eligibility status.
    """
