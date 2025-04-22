import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsAchDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    """
    Type of entity that holds the account. This can be either `individual` or `company`.
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Name of the bank associated with the bank account.
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
    Last four digits of the bank account number.
    """
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    Routing transit number of the bank account.
    """
