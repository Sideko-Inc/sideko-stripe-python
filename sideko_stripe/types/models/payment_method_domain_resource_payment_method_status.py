import pydantic
import typing
import typing_extensions

from .payment_method_domain_resource_payment_method_status_details import (
    PaymentMethodDomainResourcePaymentMethodStatusDetails,
)


class PaymentMethodDomainResourcePaymentMethodStatus(pydantic.BaseModel):
    """
    Indicates the status of a specific payment method on a payment method domain.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["active", "inactive"] = pydantic.Field(
        alias="status",
    )
    """
    The status of the payment method on the domain.
    """
    status_details: typing.Optional[
        PaymentMethodDomainResourcePaymentMethodStatusDetails
    ] = pydantic.Field(alias="status_details", default=None)
    """
    Contains additional details about the status of a payment method for a specific payment method domain.
    """
