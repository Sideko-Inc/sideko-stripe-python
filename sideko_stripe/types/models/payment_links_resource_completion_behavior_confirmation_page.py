import pydantic
import typing


class PaymentLinksResourceCompletionBehaviorConfirmationPage(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    custom_message: typing.Optional[str] = pydantic.Field(
        alias="custom_message", default=None
    )
    """
    The custom message that is displayed to the customer after the purchase is complete.
    """
