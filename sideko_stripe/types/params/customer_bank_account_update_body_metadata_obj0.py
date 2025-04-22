import pydantic
import typing
import typing_extensions


class CustomerBankAccountUpdateBodyMetadataObj0(
    typing_extensions.TypedDict, total=False
):
    """
    CustomerBankAccountUpdateBodyMetadataObj0
    """


class _SerializerCustomerBankAccountUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for CustomerBankAccountUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
