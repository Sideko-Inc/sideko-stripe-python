import pydantic
import typing

from .refund_next_action_display_details import RefundNextActionDisplayDetails


class RefundNextAction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    display_details: typing.Optional[RefundNextActionDisplayDetails] = pydantic.Field(
        alias="display_details", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    Type of the next action to perform.
    """
