import pydantic
import typing


class PaymentMethodDetailsPromptpay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Bill reference generated by PromptPay
    """
