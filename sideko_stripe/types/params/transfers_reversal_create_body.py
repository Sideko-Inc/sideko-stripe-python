import pydantic
import typing
import typing_extensions

from .transfers_reversal_create_body_metadata_obj0 import (
    TransfersReversalCreateBodyMetadataObj0,
    _SerializerTransfersReversalCreateBodyMetadataObj0,
)


class TransfersReversalCreateBody(typing_extensions.TypedDict, total=False):
    """
    TransfersReversalCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    A positive integer in cents (or local equivalent) representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string which you can attach to a reversal object. This will be unset if you POST an empty value.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[TransfersReversalCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    refund_application_fee: typing_extensions.NotRequired[bool]
    """
    Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed.
    """


class _SerializerTransfersReversalCreateBody(pydantic.BaseModel):
    """
    Serializer for TransfersReversalCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerTransfersReversalCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    refund_application_fee: typing.Optional[bool] = pydantic.Field(
        alias="refund_application_fee", default=None
    )
