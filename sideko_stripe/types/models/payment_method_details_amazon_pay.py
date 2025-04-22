import pydantic
import typing

from .amazon_pay_underlying_payment_method_funding_details import (
    AmazonPayUnderlyingPaymentMethodFundingDetails,
)


class PaymentMethodDetailsAmazonPay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    funding: typing.Optional[AmazonPayUnderlyingPaymentMethodFundingDetails] = (
        pydantic.Field(alias="funding", default=None)
    )
