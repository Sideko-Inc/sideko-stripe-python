import pydantic
import typing
import typing_extensions

from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .billing_credit_grant import BillingCreditGrant
    from .billing_credit_grants_resource_balance_credit import (
        BillingCreditGrantsResourceBalanceCredit,
    )
    from .billing_credit_grants_resource_balance_debit import (
        BillingCreditGrantsResourceBalanceDebit,
    )


class BillingCreditBalanceTransaction(pydantic.BaseModel):
    """
    A credit balance transaction is a resource representing a transaction (either a credit or a debit) against an existing credit grant.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    credit: typing.Optional["BillingCreditGrantsResourceBalanceCredit"] = (
        pydantic.Field(alias="credit", default=None)
    )
    credit_grant: typing.Union[str, "BillingCreditGrant"] = pydantic.Field(
        alias="credit_grant",
    )
    """
    The credit grant associated with this credit balance transaction.
    """
    debit: typing.Optional["BillingCreditGrantsResourceBalanceDebit"] = pydantic.Field(
        alias="debit", default=None
    )
    effective_at: int = pydantic.Field(
        alias="effective_at",
    )
    """
    The effective time of this credit balance transaction.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["billing.credit_balance_transaction"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this credit balance transaction belongs to.
    """
    type_: typing.Optional[typing_extensions.Literal["credit", "debit"]] = (
        pydantic.Field(alias="type", default=None)
    )
    """
    The type of credit balance transaction (credit or debit).
    """
