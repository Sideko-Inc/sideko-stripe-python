import pydantic
import typing
import typing_extensions

from .forwarding_request_create_body_metadata import (
    ForwardingRequestCreateBodyMetadata,
    _SerializerForwardingRequestCreateBodyMetadata,
)
from .forwarding_request_create_body_request import (
    ForwardingRequestCreateBodyRequest,
    _SerializerForwardingRequestCreateBodyRequest,
)


class ForwardingRequestCreateBody(typing_extensions.TypedDict, total=False):
    """
    ForwardingRequestCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[ForwardingRequestCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    payment_method: typing_extensions.Required[str]
    """
    The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.
    """

    replacements: typing_extensions.Required[
        typing.List[
            typing_extensions.Literal[
                "card_cvc",
                "card_expiry",
                "card_number",
                "cardholder_name",
                "request_signature",
            ]
        ]
    ]
    """
    The field kinds to be replaced in the forwarded request.
    """

    request: typing_extensions.NotRequired[ForwardingRequestCreateBodyRequest]
    """
    The request body and headers to be sent to the destination endpoint.
    """

    url: typing_extensions.Required[str]
    """
    The destination URL for the forwarded request. Must be supported by the config.
    """


class _SerializerForwardingRequestCreateBody(pydantic.BaseModel):
    """
    Serializer for ForwardingRequestCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerForwardingRequestCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    payment_method: str = pydantic.Field(
        alias="payment_method",
    )
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
    request: typing.Optional[_SerializerForwardingRequestCreateBodyRequest] = (
        pydantic.Field(alias="request", default=None)
    )
    url: str = pydantic.Field(
        alias="url",
    )
