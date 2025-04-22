import pydantic
import typing


class PaymentMethodPaypal(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the buyer's country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    payer_email: typing.Optional[str] = pydantic.Field(
        alias="payer_email", default=None
    )
    """
    Owner's email. Values are provided by PayPal directly
    (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    payer_id: typing.Optional[str] = pydantic.Field(alias="payer_id", default=None)
    """
    PayPal account PayerID. This identifier uniquely identifies the PayPal customer.
    """
