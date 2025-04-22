import pydantic
import typing

from .payment_method_details_card_present import PaymentMethodDetailsCardPresent


class CardGeneratedFromPaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_present: typing.Optional[PaymentMethodDetailsCardPresent] = pydantic.Field(
        alias="card_present", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.
    """
