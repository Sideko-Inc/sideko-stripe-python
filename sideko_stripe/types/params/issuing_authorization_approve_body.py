import pydantic
import typing
import typing_extensions

from .issuing_authorization_approve_body_metadata_obj0 import (
    IssuingAuthorizationApproveBodyMetadataObj0,
    _SerializerIssuingAuthorizationApproveBodyMetadataObj0,
)


class IssuingAuthorizationApproveBody(typing_extensions.TypedDict, total=False):
    """
    IssuingAuthorizationApproveBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    If the authorization's `pending_request.is_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization. Must be positive (use [`decline`](https://stripe.com/docs/api/issuing/authorizations/decline) to decline an authorization request).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[IssuingAuthorizationApproveBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerIssuingAuthorizationApproveBody(pydantic.BaseModel):
    """
    Serializer for IssuingAuthorizationApproveBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerIssuingAuthorizationApproveBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
