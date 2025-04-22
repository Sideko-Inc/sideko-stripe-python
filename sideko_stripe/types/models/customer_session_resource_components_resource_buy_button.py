import pydantic


class CustomerSessionResourceComponentsResourceBuyButton(pydantic.BaseModel):
    """
    This hash contains whether the buy button is enabled.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the buy button is enabled.
    """
