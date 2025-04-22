import pydantic
import typing
import typing_extensions

from .source import Source
from .source_mandate_notification_acss_debit_data import (
    SourceMandateNotificationAcssDebitData,
)
from .source_mandate_notification_bacs_debit_data import (
    SourceMandateNotificationBacsDebitData,
)
from .source_mandate_notification_sepa_debit_data import (
    SourceMandateNotificationSepaDebitData,
)


class SourceMandateNotification(pydantic.BaseModel):
    """
    Source mandate notifications should be created when a notification related to
    a source mandate must be sent to the payer. They will trigger a webhook or
    deliver an email to the customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[SourceMandateNotificationAcssDebitData] = (
        pydantic.Field(alias="acss_debit", default=None)
    )
    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount associated with the mandate notification. The amount is expressed in the currency of the underlying source. Required if the notification type is `debit_initiated`.
    """
    bacs_debit: typing.Optional[SourceMandateNotificationBacsDebitData] = (
        pydantic.Field(alias="bacs_debit", default=None)
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
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
    object: typing_extensions.Literal["source_mandate_notification"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reason: str = pydantic.Field(
        alias="reason",
    )
    """
    The reason of the mandate notification. Valid reasons are `mandate_confirmed` or `debit_initiated`.
    """
    sepa_debit: typing.Optional[SourceMandateNotificationSepaDebitData] = (
        pydantic.Field(alias="sepa_debit", default=None)
    )
    source: Source = pydantic.Field(
        alias="source",
    )
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
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the mandate notification. Valid statuses are `pending` or `submitted`.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of source this mandate notification is attached to. Should be the source type identifier code for the payment method, such as `three_d_secure`.
    """
