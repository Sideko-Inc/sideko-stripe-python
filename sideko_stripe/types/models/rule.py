import pydantic


class Rule(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action: str = pydantic.Field(
        alias="action",
    )
    """
    The action taken on the payment.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    predicate: str = pydantic.Field(
        alias="predicate",
    )
    """
    The predicate to evaluate the payment against.
    """
