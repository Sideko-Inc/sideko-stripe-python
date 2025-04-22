import pydantic
import typing
import typing_extensions


class EntitlementFeatureCreateBodyMetadata(typing_extensions.TypedDict, total=False):
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """


class _SerializerEntitlementFeatureCreateBodyMetadata(pydantic.BaseModel):
    """
    Serializer for EntitlementFeatureCreateBodyMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
