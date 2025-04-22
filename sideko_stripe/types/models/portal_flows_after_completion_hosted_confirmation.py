import pydantic
import typing


class PortalFlowsAfterCompletionHostedConfirmation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    custom_message: typing.Optional[str] = pydantic.Field(
        alias="custom_message", default=None
    )
    """
    A custom message to display to the customer after the flow is completed.
    """
