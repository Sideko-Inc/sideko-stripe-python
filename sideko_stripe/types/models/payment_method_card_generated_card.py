import pydantic
import typing
import typing_extensions

from .card_generated_from_payment_method_details import (
    CardGeneratedFromPaymentMethodDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .setup_attempt import SetupAttempt


class PaymentMethodCardGeneratedCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: typing.Optional[str] = pydantic.Field(alias="charge", default=None)
    """
    The charge that created this object.
    """
    payment_method_details: typing.Optional[CardGeneratedFromPaymentMethodDetails] = (
        pydantic.Field(alias="payment_method_details", default=None)
    )
    setup_attempt: typing.Optional[typing.Union[str, "SetupAttempt"]] = pydantic.Field(
        alias="setup_attempt", default=None
    )
    """
    The ID of the SetupAttempt that generated this PaymentMethod, if any.
    """
