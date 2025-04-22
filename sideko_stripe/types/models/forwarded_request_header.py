import pydantic


class ForwardedRequestHeader(pydantic.BaseModel):
    """
    Header data.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    """
    The header name.
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    The header value.
    """
