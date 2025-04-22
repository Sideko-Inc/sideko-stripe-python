import pydantic
import typing
import typing_extensions

from .forwarded_request_header import ForwardedRequestHeader


class ForwardedRequestDetails(pydantic.BaseModel):
    """
    Details about the request forwarded to the destination endpoint.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    body: str = pydantic.Field(
        alias="body",
    )
    """
    The body payload to send to the destination endpoint.
    """
    headers: typing.List[ForwardedRequestHeader] = pydantic.Field(
        alias="headers",
    )
    """
    The headers to include in the forwarded request. Can be omitted if no additional headers (excluding Stripe-generated ones such as the Content-Type header) should be included.
    """
    http_method: typing_extensions.Literal["POST"] = pydantic.Field(
        alias="http_method",
    )
    """
    The HTTP method used to call the destination endpoint.
    """
