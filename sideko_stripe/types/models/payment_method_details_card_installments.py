import pydantic
import typing

from .payment_method_details_card_installments_plan import (
    PaymentMethodDetailsCardInstallmentsPlan,
)


class PaymentMethodDetailsCardInstallments(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    plan: typing.Optional[PaymentMethodDetailsCardInstallmentsPlan] = pydantic.Field(
        alias="plan", default=None
    )
