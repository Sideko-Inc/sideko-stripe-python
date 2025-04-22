import pydantic
import typing
import typing_extensions


class ForwardingRequestCreateBodyMetadata(typing_extensions.TypedDict, total=False):
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerForwardingRequestCreateBodyMetadata(pydantic.BaseModel):
    """
    Serializer for ForwardingRequestCreateBodyMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
