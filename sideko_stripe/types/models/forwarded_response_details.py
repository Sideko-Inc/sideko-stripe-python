import pydantic
import typing

from .forwarded_request_header import ForwardedRequestHeader


class ForwardedResponseDetails(pydantic.BaseModel):
    """
    Details about the response from the destination endpoint.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    body: str = pydantic.Field(
        alias="body",
    )
    """
    The response body from the destination endpoint to Stripe.
    """
    headers: typing.List[ForwardedRequestHeader] = pydantic.Field(
        alias="headers",
    )
    """
    HTTP headers that the destination endpoint returned.
    """
    status: int = pydantic.Field(
        alias="status",
    )
    """
    The HTTP status code that the destination endpoint returned.
    """
