import pydantic
import typing
import typing_extensions

from .payment_links_resource_payment_method_reuse_agreement import (
    PaymentLinksResourcePaymentMethodReuseAgreement,
)


class PaymentLinksResourceConsentCollection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_method_reuse_agreement: typing.Optional[
        PaymentLinksResourcePaymentMethodReuseAgreement
    ] = pydantic.Field(alias="payment_method_reuse_agreement", default=None)
    promotions: typing.Optional[typing_extensions.Literal["auto", "none"]] = (
        pydantic.Field(alias="promotions", default=None)
    )
    """
    If set to `auto`, enables the collection of customer consent for promotional communications.
    """
    terms_of_service: typing.Optional[typing_extensions.Literal["none", "required"]] = (
        pydantic.Field(alias="terms_of_service", default=None)
    )
    """
    If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won't be shown a checkbox to accept the terms of service.
    """
