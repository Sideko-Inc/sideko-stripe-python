import pydantic
import typing
import typing_extensions

from .forwarded_request_context import ForwardedRequestContext
from .forwarded_request_details import ForwardedRequestDetails
from .forwarded_response_details import ForwardedResponseDetails
from .forwarding_request_metadata import ForwardingRequestMetadata


class ForwardingRequest(pydantic.BaseModel):
    """
    Instructs Stripe to make a request on your behalf using the destination URL. The destination URL
    is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials
    provided during onboarding, and injects card details from the payment_method into the request.

    Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers,
    before storing the request and response data in the forwarding Request object, which are subject to a
    30-day retention period.

    You can provide a Stripe idempotency key to make sure that requests with the same key result in only one
    outbound request. The Stripe idempotency key provided should be unique and different from any idempotency
    keys provided on the underlying third-party request.

    Forwarding Requests are synchronous requests that return a response or time out according to
    Stripe’s limits.

    Related guide: [Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding).
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
    metadata: typing.Optional[ForwardingRequestMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["forwarding.request"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method: str = pydantic.Field(
        alias="payment_method",
    )
    """
    The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.
    """
    replacements: typing.List[
        typing_extensions.Literal[
            "card_cvc",
            "card_expiry",
            "card_number",
            "cardholder_name",
            "request_signature",
        ]
    ] = pydantic.Field(
        alias="replacements",
    )
    """
    The field kinds to be replaced in the forwarded request.
    """
    request_context: typing.Optional[ForwardedRequestContext] = pydantic.Field(
        alias="request_context", default=None
    )
    """
    Metadata about the forwarded request.
    """
    request_details: typing.Optional[ForwardedRequestDetails] = pydantic.Field(
        alias="request_details", default=None
    )
    """
    Details about the request forwarded to the destination endpoint.
    """
    response_details: typing.Optional[ForwardedResponseDetails] = pydantic.Field(
        alias="response_details", default=None
    )
    """
    Details about the response from the destination endpoint.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The destination URL for the forwarded request. Must be supported by the config.
    """
