import pydantic
import typing
import typing_extensions

from .source import Source
from .topup_metadata import TopupMetadata

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction


class Topup(pydantic.BaseModel):
    """
    To top up your Stripe balance, you create a top-up object. You can retrieve
    individual top-ups, as well as list all top-ups. Top-ups are identified by a
    unique, random ID.

    Related guide: [Topping up your platform account](https://stripe.com/docs/connect/top-ups)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount transferred.
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    ID of the balance transaction that describes the impact of this top-up on your account balance. May not be specified depending on status of top-up.
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
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expected_availability_date: typing.Optional[int] = pydantic.Field(
        alias="expected_availability_date", default=None
    )
    """
    Date the funds are expected to arrive in your Stripe account for payouts. This factors in delays like weekends or bank holidays. May not be specified depending on status of top-up.
    """
    failure_code: typing.Optional[str] = pydantic.Field(
        alias="failure_code", default=None
    )
    """
    Error code explaining reason for top-up failure if available (see [the errors section](https://stripe.com/docs/api#errors) for a list of codes).
    """
    failure_message: typing.Optional[str] = pydantic.Field(
        alias="failure_message", default=None
    )
    """
    Message to user further explaining reason for top-up failure if available.
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
    metadata: TopupMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["topup"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    source: typing.Optional[Source] = pydantic.Field(alias="source", default=None)
    """
    `Source` objects allow you to accept a variety of payment methods. They
    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.
    
    Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
    This newer API provides access to our latest features and payment method types.
    
    Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    Extra information about a top-up. This will appear on your source's bank statement. It must contain at least one letter.
    """
    status: typing_extensions.Literal[
        "canceled", "failed", "pending", "reversed", "succeeded"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`, or `succeeded`.
    """
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
    """
    A string that identifies this top-up as part of a group.
    """
