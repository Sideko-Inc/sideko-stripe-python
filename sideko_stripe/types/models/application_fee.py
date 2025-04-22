import pydantic
import typing
import typing_extensions

from .application import Application
from .platform_earning_fee_source import PlatformEarningFeeSource

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .application_fee_refunds import ApplicationFeeRefunds
    from .balance_transaction import BalanceTransaction
    from .charge import Charge


class ApplicationFee(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Union[str, "Account"] = pydantic.Field(
        alias="account",
    )
    """
    ID of the Stripe account this fee was taken from.
    """
    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount earned, in cents (or local equivalent).
    """
    amount_refunded: int = pydantic.Field(
        alias="amount_refunded",
    )
    """
    Amount in cents (or local equivalent) refunded (can be less than the amount attribute on the fee if a partial refund was issued)
    """
    application: typing.Union[str, Application] = pydantic.Field(
        alias="application",
    )
    """
    ID of the Connect application that earned the fee.
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    Balance transaction that describes the impact of this collected application fee on your account balance (not including refunds).
    """
    charge: typing.Union[str, "Charge"] = pydantic.Field(
        alias="charge",
    )
    """
    ID of the charge that the application fee was taken from.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    fee_source: typing.Optional[PlatformEarningFeeSource] = pydantic.Field(
        alias="fee_source", default=None
    )
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
    object: typing_extensions.Literal["application_fee"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    originating_transaction: typing.Optional[typing.Union[str, "Charge"]] = (
        pydantic.Field(alias="originating_transaction", default=None)
    )
    """
    ID of the corresponding charge on the platform account, if this fee was the result of a charge using the `destination` parameter.
    """
    refunded: bool = pydantic.Field(
        alias="refunded",
    )
    """
    Whether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false.
    """
    refunds: "ApplicationFeeRefunds" = pydantic.Field(
        alias="refunds",
    )
    """
    A list of refunds that have been applied to the fee.
    """
