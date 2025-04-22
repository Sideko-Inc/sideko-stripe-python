import pydantic


class CustomerSessionResourceComponentsResourcePricingTable(pydantic.BaseModel):
    """
    This hash contains whether the pricing table is enabled.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the pricing table is enabled.
    """
