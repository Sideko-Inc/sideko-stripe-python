import pydantic
import typing


class PaymentMethodDetailsAcssDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Name of the bank associated with the bank account.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    institution_number: typing.Optional[str] = pydantic.Field(
        alias="institution_number", default=None
    )
    """
    Institution number of the bank account
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last four digits of the bank account number.
    """
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    """
    ID of the mandate used to make this payment.
    """
    transit_number: typing.Optional[str] = pydantic.Field(
        alias="transit_number", default=None
    )
    """
    Transit number of the bank account.
    """
