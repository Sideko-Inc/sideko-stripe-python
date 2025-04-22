import pydantic
import typing
import typing_extensions

from .credit_balance import CreditBalance
from .deleted_customer import DeletedCustomer

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer


class BillingCreditBalanceSummary(pydantic.BaseModel):
    """
    Indicates the billing credit balance for billing credits granted to a customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    balances: typing.List[CreditBalance] = pydantic.Field(
        alias="balances",
    )
    """
    The billing credit balances. One entry per credit grant currency. If a customer only has credit grants in a single currency, then this will have a single balance entry.
    """
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    The customer the balance is for.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["billing.credit_balance_summary"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
