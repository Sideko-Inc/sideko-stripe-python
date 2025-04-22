import pydantic
import typing
import typing_extensions

from .balance_amount import BalanceAmount
from .balance_amount_net import BalanceAmountNet
from .balance_detail import BalanceDetail


class Balance(pydantic.BaseModel):
    """
    This is an object representing your Stripe balance. You can retrieve it to see
    the balance currently on your Stripe account.

    You can also retrieve the balance history, which contains a list of
    [transactions](https://stripe.com/docs/reporting/balance-transaction-types) that contributed to the balance
    (charges, payouts, and so forth).

    The available and pending amounts for each currency are broken down further by
    payment source types.

    Related guide: [Understanding Connect account balances](https://stripe.com/docs/connect/account-balances)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: typing.List[BalanceAmount] = pydantic.Field(
        alias="available",
    )
    """
    Available funds that you can transfer or pay out automatically by Stripe or explicitly through the [Transfers API](https://stripe.com/docs/api#transfers) or [Payouts API](https://stripe.com/docs/api#payouts). You can find the available balance for each currency and payment type in the `source_types` property.
    """
    connect_reserved: typing.Optional[typing.List[BalanceAmount]] = pydantic.Field(
        alias="connect_reserved", default=None
    )
    """
    Funds held due to negative balances on connected accounts where [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. You can find the connect reserve balance for each currency and payment type in the `source_types` property.
    """
    instant_available: typing.Optional[typing.List[BalanceAmountNet]] = pydantic.Field(
        alias="instant_available", default=None
    )
    """
    Funds that you can pay out using Instant Payouts.
    """
    issuing: typing.Optional[BalanceDetail] = pydantic.Field(
        alias="issuing", default=None
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["balance"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending: typing.List[BalanceAmount] = pydantic.Field(
        alias="pending",
    )
    """
    Funds that aren't available in the balance yet. You can find the pending balance for each currency and each payment type in the `source_types` property.
    """
