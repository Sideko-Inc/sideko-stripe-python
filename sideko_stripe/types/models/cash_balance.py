import pydantic
import typing
import typing_extensions

from .cash_balance_available import CashBalanceAvailable
from .customer_balance_customer_balance_settings import (
    CustomerBalanceCustomerBalanceSettings,
)


class CashBalance(pydantic.BaseModel):
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: typing.Optional[CashBalanceAvailable] = pydantic.Field(
        alias="available", default=None
    )
    """
    A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    customer: str = pydantic.Field(
        alias="customer",
    )
    """
    The ID of the customer whose cash balance this object represents.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["cash_balance"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    settings: CustomerBalanceCustomerBalanceSettings = pydantic.Field(
        alias="settings",
    )
