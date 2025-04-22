import pydantic
import typing

from .payment_method_options_card_present_routing import (
    PaymentMethodOptionsCardPresentRouting,
)


class PaymentMethodOptionsCardPresent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    request_extended_authorization: typing.Optional[bool] = pydantic.Field(
        alias="request_extended_authorization", default=None
    )
    """
    Request ability to capture this payment beyond the standard [authorization validity window](https://stripe.com/docs/terminal/features/extended-authorizations#authorization-validity)
    """
    request_incremental_authorization_support: typing.Optional[bool] = pydantic.Field(
        alias="request_incremental_authorization_support", default=None
    )
    """
    Request ability to [increment](https://stripe.com/docs/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://stripe.com/docs/api/payment_intents/confirm) response to verify support.
    """
    routing: typing.Optional[PaymentMethodOptionsCardPresentRouting] = pydantic.Field(
        alias="routing", default=None
    )
