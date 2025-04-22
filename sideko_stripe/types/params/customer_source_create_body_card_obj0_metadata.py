import pydantic
import typing
import typing_extensions


class CustomerSourceCreateBodyCardObj0Metadata(
    typing_extensions.TypedDict, total=False
):
    """
    CustomerSourceCreateBodyCardObj0Metadata
    """


class _SerializerCustomerSourceCreateBodyCardObj0Metadata(pydantic.BaseModel):
    """
    Serializer for CustomerSourceCreateBodyCardObj0Metadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
