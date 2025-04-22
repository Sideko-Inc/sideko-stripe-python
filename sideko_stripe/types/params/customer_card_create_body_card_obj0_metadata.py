import pydantic
import typing
import typing_extensions


class CustomerCardCreateBodyCardObj0Metadata(typing_extensions.TypedDict, total=False):
    """
    CustomerCardCreateBodyCardObj0Metadata
    """


class _SerializerCustomerCardCreateBodyCardObj0Metadata(pydantic.BaseModel):
    """
    Serializer for CustomerCardCreateBodyCardObj0Metadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
