import pydantic
import typing
import typing_extensions

from .payment_pages_checkout_session_payment_method_reuse_agreement import (
    PaymentPagesCheckoutSessionPaymentMethodReuseAgreement,
)


class PaymentPagesCheckoutSessionConsentCollection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_method_reuse_agreement: typing.Optional[
        PaymentPagesCheckoutSessionPaymentMethodReuseAgreement
    ] = pydantic.Field(alias="payment_method_reuse_agreement", default=None)
    promotions: typing.Optional[typing_extensions.Literal["auto", "none"]] = (
        pydantic.Field(alias="promotions", default=None)
    )
    """
    If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout
    Session will determine whether to display an option to opt into promotional communication
    from the merchant depending on the customer's locale. Only available to US merchants.
    """
    terms_of_service: typing.Optional[typing_extensions.Literal["none", "required"]] = (
        pydantic.Field(alias="terms_of_service", default=None)
    )
    """
    If set to `required`, it requires customers to accept the terms of service before being able to pay.
    """
