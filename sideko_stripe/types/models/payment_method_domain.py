import pydantic
import typing_extensions

from .payment_method_domain_resource_payment_method_status import (
    PaymentMethodDomainResourcePaymentMethodStatus,
)


class PaymentMethodDomain(pydantic.BaseModel):
    """
    A payment method domain represents a web domain that you have registered with Stripe.
    Stripe Elements use registered payment method domains to control where certain payment methods are shown.

    Related guide: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amazon_pay: PaymentMethodDomainResourcePaymentMethodStatus = pydantic.Field(
        alias="amazon_pay",
    )
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    apple_pay: PaymentMethodDomainResourcePaymentMethodStatus = pydantic.Field(
        alias="apple_pay",
    )
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    domain_name: str = pydantic.Field(
        alias="domain_name",
    )
    """
    The domain name that this payment method domain object represents.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.
    """
    google_pay: PaymentMethodDomainResourcePaymentMethodStatus = pydantic.Field(
        alias="google_pay",
    )
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    link: PaymentMethodDomainResourcePaymentMethodStatus = pydantic.Field(
        alias="link",
    )
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["payment_method_domain"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    paypal: PaymentMethodDomainResourcePaymentMethodStatus = pydantic.Field(
        alias="paypal",
    )
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
