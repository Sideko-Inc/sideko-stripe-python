import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .sepa_debit_generated_from import SepaDebitGeneratedFrom


class PaymentMethodSepaDebit(pydantic.BaseModel):
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
    generated_from: typing.Optional["SepaDebitGeneratedFrom"] = pydantic.Field(
        alias="generated_from", default=None
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last four characters of the IBAN.
    """
