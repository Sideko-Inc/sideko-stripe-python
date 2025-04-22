import pydantic
import typing
import typing_extensions


class CustomerUpdateBodyCardObj0Metadata(typing_extensions.TypedDict, total=False):
    """
    CustomerUpdateBodyCardObj0Metadata
    """


class _SerializerCustomerUpdateBodyCardObj0Metadata(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBodyCardObj0Metadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
