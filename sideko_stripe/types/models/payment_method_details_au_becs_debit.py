import pydantic
import typing


class PaymentMethodDetailsAuBecsDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bsb_number: typing.Optional[str] = pydantic.Field(alias="bsb_number", default=None)
    """
    Bank-State-Branch number of the bank account.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last four digits of the bank account number.
    """
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    """
    ID of the mandate used to make this payment.
    """
