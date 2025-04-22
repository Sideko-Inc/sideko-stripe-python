import pydantic
import typing

from .revolut_pay_underlying_payment_method_funding_details import (
    RevolutPayUnderlyingPaymentMethodFundingDetails,
)


class PaymentMethodDetailsRevolutPay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    funding: typing.Optional[RevolutPayUnderlyingPaymentMethodFundingDetails] = (
        pydantic.Field(alias="funding", default=None)
    )
