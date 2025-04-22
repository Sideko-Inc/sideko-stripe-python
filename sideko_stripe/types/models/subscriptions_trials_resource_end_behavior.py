import pydantic
import typing_extensions


class SubscriptionsTrialsResourceEndBehavior(pydantic.BaseModel):
    """
    Defines how a subscription behaves when a free trial ends.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    missing_payment_method: typing_extensions.Literal[
        "cancel", "create_invoice", "pause"
    ] = pydantic.Field(
        alias="missing_payment_method",
    )
    """
    Indicates how the subscription should change when the trial ends if the user did not provide a payment method.
    """
