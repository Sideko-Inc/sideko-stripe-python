import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .mandate import Mandate


class OutboundPaymentsPaymentMethodDetailsUsBankAccount(pydantic.BaseModel):
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
    Name of the bank associated with the bank account.
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
    mandate: typing.Optional[typing.Union[str, "Mandate"]] = pydantic.Field(
        alias="mandate", default=None
    )
    """
    ID of the mandate used to make this payment.
    """
    network: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="network",
    )
    """
    The network rails used. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type.
    """
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    Routing number of the bank account.
    """
