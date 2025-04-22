import pydantic
import typing
import typing_extensions

from .webhook_endpoint_metadata import WebhookEndpointMetadata


class WebhookEndpoint(pydantic.BaseModel):
    """
    You can configure [webhook endpoints](https://docs.stripe.com/webhooks/) via the API to be
    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up webhooks](https://docs.stripe.com/webhooks/configure)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    api_version: typing.Optional[str] = pydantic.Field(
        alias="api_version", default=None
    )
    """
    The API version events are rendered as for this webhook endpoint.
    """
    application: typing.Optional[str] = pydantic.Field(
        alias="application", default=None
    )
    """
    The ID of the associated Connect application.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An optional description of what the webhook is used for.
    """
    enabled_events: typing.List[str] = pydantic.Field(
        alias="enabled_events",
    )
    """
    The list of events to enable for this endpoint. `['*']` indicates that all events are enabled, except those that require explicit selection.
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
    metadata: WebhookEndpointMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["webhook_endpoint"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    secret: typing.Optional[str] = pydantic.Field(alias="secret", default=None)
    """
    The endpoint's secret, used to generate [webhook signatures](https://docs.stripe.com/webhooks/signatures). Only returned at creation.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the webhook. It can be `enabled` or `disabled`.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL of the webhook endpoint.
    """
