import pydantic
import typing
import typing_extensions


class SubscriptionItemUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    SubscriptionItemUpdateBodyMetadataObj0
    """


class _SerializerSubscriptionItemUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for SubscriptionItemUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
