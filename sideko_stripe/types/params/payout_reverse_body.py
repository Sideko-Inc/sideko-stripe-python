import pydantic
import typing
import typing_extensions

from .payout_reverse_body_metadata import (
    PayoutReverseBodyMetadata,
    _SerializerPayoutReverseBodyMetadata,
)


class PayoutReverseBody(typing_extensions.TypedDict, total=False):
    """
    PayoutReverseBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[PayoutReverseBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerPayoutReverseBody(pydantic.BaseModel):
    """
    Serializer for PayoutReverseBody handling case conversions
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
    metadata: typing.Optional[_SerializerPayoutReverseBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
