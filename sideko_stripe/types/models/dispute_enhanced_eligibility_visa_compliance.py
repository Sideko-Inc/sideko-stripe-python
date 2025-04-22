import pydantic
import typing_extensions


class DisputeEnhancedEligibilityVisaCompliance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal[
        "fee_acknowledged", "requires_fee_acknowledgement"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Visa compliance eligibility status.
    """
