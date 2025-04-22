import pydantic


class ClimateRemovalsBeneficiary(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    public_name: str = pydantic.Field(
        alias="public_name",
    )
    """
    Publicly displayable name for the end beneficiary of carbon removal.
    """
