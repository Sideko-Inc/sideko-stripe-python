import pydantic


class PortalFlowsAfterCompletionRedirect(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    return_url: str = pydantic.Field(
        alias="return_url",
    )
    """
    The URL the customer will be redirected to after the flow is completed.
    """
