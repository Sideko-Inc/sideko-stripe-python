import pydantic


class BillingClocksResourceStatusDetailsAdvancingStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    target_frozen_time: int = pydantic.Field(
        alias="target_frozen_time",
    )
    """
    The `frozen_time` that the Test Clock is advancing towards.
    """
