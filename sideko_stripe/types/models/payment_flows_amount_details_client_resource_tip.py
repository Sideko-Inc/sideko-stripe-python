import pydantic
import typing


class PaymentFlowsAmountDetailsClientResourceTip(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    Portion of the amount that corresponds to a tip.
    """
