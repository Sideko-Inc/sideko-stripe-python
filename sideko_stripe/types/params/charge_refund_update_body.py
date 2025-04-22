import pydantic
import typing
import typing_extensions

from .charge_refund_update_body_metadata_obj0 import (
    ChargeRefundUpdateBodyMetadataObj0,
    _SerializerChargeRefundUpdateBodyMetadataObj0,
)


class ChargeRefundUpdateBody(typing_extensions.TypedDict, total=False):
    """
    ChargeRefundUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ChargeRefundUpdateBodyMetadataObj0, str]
    ]


class _SerializerChargeRefundUpdateBody(pydantic.BaseModel):
    """
    Serializer for ChargeRefundUpdateBody handling case conversions
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
    metadata: typing.Optional[
        typing.Union[_SerializerChargeRefundUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
