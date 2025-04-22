import pydantic
import typing


class NotificationEventRequest(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the API request that caused the event. If null, the event was automatic (e.g., Stripe's automatic subscription handling). Request logs are available in the [dashboard](https://dashboard.stripe.com/logs), but currently not in the API.
    """
    idempotency_key: typing.Optional[str] = pydantic.Field(
        alias="idempotency_key", default=None
    )
    """
    The idempotency key transmitted during the request, if any. *Note: This property is populated only for events on or after May 23, 2017*.
    """
