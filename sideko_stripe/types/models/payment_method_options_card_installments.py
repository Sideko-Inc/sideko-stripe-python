import pydantic
import typing

from .payment_method_details_card_installments_plan import (
    PaymentMethodDetailsCardInstallmentsPlan,
)


class PaymentMethodOptionsCardInstallments(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available_plans: typing.Optional[
        typing.List[PaymentMethodDetailsCardInstallmentsPlan]
    ] = pydantic.Field(alias="available_plans", default=None)
    """
    Installment plans that may be selected for this PaymentIntent.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether Installments are enabled for this PaymentIntent.
    """
    plan: typing.Optional[PaymentMethodDetailsCardInstallmentsPlan] = pydantic.Field(
        alias="plan", default=None
    )
