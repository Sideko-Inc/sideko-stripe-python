import pydantic
import typing
import typing_extensions

from .forwarding_request_create_body_request_headers_item import (
    ForwardingRequestCreateBodyRequestHeadersItem,
    _SerializerForwardingRequestCreateBodyRequestHeadersItem,
)


class ForwardingRequestCreateBodyRequest(typing_extensions.TypedDict):
    """
    The request body and headers to be sent to the destination endpoint.
    """

    body: typing_extensions.NotRequired[str]

    headers: typing_extensions.NotRequired[
        typing.List[ForwardingRequestCreateBodyRequestHeadersItem]
    ]


class _SerializerForwardingRequestCreateBodyRequest(pydantic.BaseModel):
    """
    Serializer for ForwardingRequestCreateBodyRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    body: typing.Optional[str] = pydantic.Field(alias="body", default=None)
    headers: typing.Optional[
        typing.List[_SerializerForwardingRequestCreateBodyRequestHeadersItem]
    ] = pydantic.Field(alias="headers", default=None)
