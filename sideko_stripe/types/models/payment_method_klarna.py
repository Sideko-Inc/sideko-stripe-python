import pydantic
import typing

from .payment_flows_private_payment_methods_klarna_dob import (
    PaymentFlowsPrivatePaymentMethodsKlarnaDob,
)


class PaymentMethodKlarna(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dob: typing.Optional[PaymentFlowsPrivatePaymentMethodsKlarnaDob] = pydantic.Field(
        alias="dob", default=None
    )
