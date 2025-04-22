import pydantic

from .payment_method_config_resource_display_preference import (
    PaymentMethodConfigResourceDisplayPreference,
)


class PaymentMethodConfigResourcePaymentMethodProperties(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: bool = pydantic.Field(
        alias="available",
    )
    """
    Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
    """
    display_preference: PaymentMethodConfigResourceDisplayPreference = pydantic.Field(
        alias="display_preference",
    )
