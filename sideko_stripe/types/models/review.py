import pydantic
import typing
import typing_extensions

from .radar_review_resource_location import RadarReviewResourceLocation
from .radar_review_resource_session import RadarReviewResourceSession

if typing_extensions.TYPE_CHECKING:
    from .charge import Charge
    from .payment_intent import PaymentIntent


class Review(pydantic.BaseModel):
    """
    Reviews can be used to supplement automated fraud detection with human expertise.

    Learn more about [Radar](/radar) and reviewing payments
    [here](https://stripe.com/docs/radar/reviews).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_zip: typing.Optional[str] = pydantic.Field(
        alias="billing_zip", default=None
    )
    """
    The ZIP or postal code of the card used, if applicable.
    """
    charge: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="charge", default=None
    )
    """
    The charge associated with this review.
    """
    closed_reason: typing.Optional[
        typing_extensions.Literal[
            "approved",
            "canceled",
            "disputed",
            "redacted",
            "refunded",
            "refunded_as_fraud",
        ]
    ] = pydantic.Field(alias="closed_reason", default=None)
    """
    The reason the review was closed, or null if it has not yet been closed. One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, `redacted`, or `canceled`.
    """
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
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The IP address where the payment originated.
    """
    ip_address_location: typing.Optional[RadarReviewResourceLocation] = pydantic.Field(
        alias="ip_address_location", default=None
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["review"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    open: bool = pydantic.Field(
        alias="open",
    )
    """
    If `true`, the review needs action.
    """
    opened_reason: typing_extensions.Literal["manual", "rule"] = pydantic.Field(
        alias="opened_reason",
    )
    """
    The reason the review was opened. One of `rule` or `manual`.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    The PaymentIntent ID associated with this review, if one exists.
    """
    reason: str = pydantic.Field(
        alias="reason",
    )
    """
    The reason the review is currently open or closed. One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`, `disputed`, `redacted`, or `canceled`.
    """
    session: typing.Optional[RadarReviewResourceSession] = pydantic.Field(
        alias="session", default=None
    )
