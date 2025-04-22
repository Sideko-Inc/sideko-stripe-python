import pydantic
import typing
import typing_extensions

from .payment_intent_card_processing import PaymentIntentCardProcessing


class PaymentIntentProcessing(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card: typing.Optional[PaymentIntentCardProcessing] = pydantic.Field(
        alias="card", default=None
    )
    type_: typing_extensions.Literal["card"] = pydantic.Field(
        alias="type",
    )
    """
    Type of the payment method for which payment is in `processing` state, one of `card`.
    """
