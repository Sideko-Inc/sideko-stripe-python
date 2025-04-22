import pydantic
import typing
import typing_extensions

from .notification_event_data import NotificationEventData
from .notification_event_request import NotificationEventRequest


class Event(pydantic.BaseModel):
    """
    Events are our way of letting you know when something interesting happens in
    your account. When an interesting event occurs, we create a new `Event`
    object. For example, when a charge succeeds, we create a `charge.succeeded`
    event, and when an invoice payment attempt fails, we create an
    `invoice.payment_failed` event. Certain API requests might create multiple
    events. For example, if you create a new subscription for a
    customer, you receive both a `customer.subscription.created` event and a
    `charge.succeeded` event.

    Events occur when the state of another API resource changes. The event's data
    field embeds the resource's state at the time of the change. For
    example, a `charge.succeeded` event contains a charge, and an
    `invoice.payment_failed` event contains an invoice.

    As with other API resources, you can use endpoints to retrieve an
    [individual event](https://stripe.com/docs/api#retrieve_event) or a [list of events](https://stripe.com/docs/api#list_events)
    from the API. We also have a separate
    [webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the
    `Event` objects directly to an endpoint on your server. You can manage
    webhooks in your
    [account settings](https://dashboard.stripe.com/account/webhooks). Learn how
    to [listen for events](https://docs.stripe.com/webhooks)
    so that your integration can automatically trigger reactions.

    When using [Connect](https://docs.stripe.com/connect), you can also receive event notifications
    that occur in connected accounts. For these events, there's an
    additional `account` attribute in the received `Event` object.

    We only guarantee access to events through the [Retrieve Event API](https://stripe.com/docs/api#retrieve_event)
    for 30 days.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    """
    The connected account that originates the event.
    """
    api_version: typing.Optional[str] = pydantic.Field(
        alias="api_version", default=None
    )
    """
    The Stripe API version used to render `data`. This property is populated only for events on or after October 31, 2014.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    data: NotificationEventData = pydantic.Field(
        alias="data",
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
    object: typing_extensions.Literal["event"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending_webhooks: int = pydantic.Field(
        alias="pending_webhooks",
    )
    """
    Number of webhooks that haven't been successfully delivered (for example, to return a 20x response) to the URLs you specify.
    """
    request: typing.Optional[NotificationEventRequest] = pydantic.Field(
        alias="request", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    Description of the event (for example, `invoice.created` or `charge.refunded`).
    """
