import pydantic
import typing


class PaymentMethodDetailsSepaDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    """
    Bank code of bank associated with the bank account.
    """
    branch_code: typing.Optional[str] = pydantic.Field(
        alias="branch_code", default=None
    )
    """
    Branch code of bank associated with the bank account.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country the bank account is located in.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last four characters of the IBAN.
    """
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    """
    Find the ID of the mandate used for this payment under the [payment_method_details.sepa_debit.mandate](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate) property on the Charge. Use this mandate ID to [retrieve the Mandate](https://stripe.com/docs/api/mandates/retrieve).
    """
