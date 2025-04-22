import pydantic
import typing

from .confirmation_tokens_resource_payment_method_options_resource_card import (
    ConfirmationTokensResourcePaymentMethodOptionsResourceCard,
)


class ConfirmationTokensResourcePaymentMethodOptions(pydantic.BaseModel):
    """
    Payment-method-specific configuration
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card: typing.Optional[
        ConfirmationTokensResourcePaymentMethodOptionsResourceCard
    ] = pydantic.Field(alias="card", default=None)
    """
    This hash contains the card payment method options.
    """
