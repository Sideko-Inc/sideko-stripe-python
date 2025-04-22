import pydantic
import typing
import typing_extensions


class SourceCreateBodyReceiver(typing_extensions.TypedDict):
    """
    Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`).
    """

    refund_attributes_method: typing_extensions.NotRequired[
        typing_extensions.Literal["email", "manual", "none"]
    ]


class _SerializerSourceCreateBodyReceiver(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyReceiver handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    refund_attributes_method: typing.Optional[
        typing_extensions.Literal["email", "manual", "none"]
    ] = pydantic.Field(alias="refund_attributes_method", default=None)
