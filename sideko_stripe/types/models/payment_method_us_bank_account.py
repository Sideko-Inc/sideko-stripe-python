import pydantic
import typing
import typing_extensions

from .payment_method_us_bank_account_status_details import (
    PaymentMethodUsBankAccountStatusDetails,
)
from .us_bank_account_networks import UsBankAccountNetworks


class PaymentMethodUsBankAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    """
    Account holder type: individual or company.
    """
    account_type: typing.Optional[typing_extensions.Literal["checking", "savings"]] = (
        pydantic.Field(alias="account_type", default=None)
    )
    """
    Account type: checkings or savings. Defaults to checking if omitted.
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    The name of the bank.
    """
    financial_connections_account: typing.Optional[str] = pydantic.Field(
        alias="financial_connections_account", default=None
    )
    """
    The ID of the Financial Connections Account used to create the payment method.
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
    networks: typing.Optional[UsBankAccountNetworks] = pydantic.Field(
        alias="networks", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    Routing number of the bank account.
    """
    status_details: typing.Optional[PaymentMethodUsBankAccountStatusDetails] = (
        pydantic.Field(alias="status_details", default=None)
    )
