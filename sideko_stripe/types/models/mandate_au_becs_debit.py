import pydantic


class MandateAuBecsDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.
    """
