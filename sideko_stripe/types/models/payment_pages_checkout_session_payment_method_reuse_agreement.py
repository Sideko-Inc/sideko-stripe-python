import pydantic
import typing_extensions


class PaymentPagesCheckoutSessionPaymentMethodReuseAgreement(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    position: typing_extensions.Literal["auto", "hidden"] = pydantic.Field(
        alias="position",
    )
    """
    Determines the position and visibility of the payment method reuse agreement in the UI. When set to `auto`, Stripe's defaults will be used.
    
    When set to `hidden`, the payment method reuse agreement text will always be hidden in the UI.
    """
