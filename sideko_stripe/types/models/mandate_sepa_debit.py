import pydantic


class MandateSepaDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: str = pydantic.Field(
        alias="reference",
    )
    """
    The unique reference of the mandate.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.
    """
