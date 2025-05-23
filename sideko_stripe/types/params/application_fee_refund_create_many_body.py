import pydantic
import typing
import typing_extensions

from .application_fee_refund_create_many_body_metadata import (
    ApplicationFeeRefundCreateManyBodyMetadata,
    _SerializerApplicationFeeRefundCreateManyBodyMetadata,
)


class ApplicationFeeRefundCreateManyBody(typing_extensions.TypedDict, total=False):
    """
    ApplicationFeeRefundCreateManyBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    A positive integer, in _cents (or local equivalent)_, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[ApplicationFeeRefundCreateManyBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerApplicationFeeRefundCreateManyBody(pydantic.BaseModel):
    """
    Serializer for ApplicationFeeRefundCreateManyBody handling case conversions
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
    metadata: typing.Optional[_SerializerApplicationFeeRefundCreateManyBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
