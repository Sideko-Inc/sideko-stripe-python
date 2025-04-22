import pydantic
import typing


class PaymentMethodDetailsAffirm(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    transaction_id: typing.Optional[str] = pydantic.Field(
        alias="transaction_id", default=None
    )
    """
    The Affirm transaction ID associated with this payment.
    """
