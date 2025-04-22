import pydantic
import typing
import typing_extensions


class SubscriptionCreateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    SubscriptionCreateBodyMetadataObj0
    """


class _SerializerSubscriptionCreateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
