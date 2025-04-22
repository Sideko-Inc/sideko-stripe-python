import pydantic
import typing


class PaymentMethodDetailsSwish(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies the payer's Swish account. You can use this attribute to check whether two Swish transactions were paid for by the same payer
    """
    payment_reference: typing.Optional[str] = pydantic.Field(
        alias="payment_reference", default=None
    )
    """
    Payer bank reference number for the payment
    """
    verified_phone_last4: typing.Optional[str] = pydantic.Field(
        alias="verified_phone_last4", default=None
    )
    """
    The last four digits of the Swish account phone number
    """
