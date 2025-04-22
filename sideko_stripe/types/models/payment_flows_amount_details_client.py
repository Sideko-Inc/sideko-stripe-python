import pydantic
import typing

from .payment_flows_amount_details_client_resource_tip import (
    PaymentFlowsAmountDetailsClientResourceTip,
)


class PaymentFlowsAmountDetailsClient(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tip: typing.Optional[PaymentFlowsAmountDetailsClientResourceTip] = pydantic.Field(
        alias="tip", default=None
    )
