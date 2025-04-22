import pydantic
import typing
import typing_extensions


class CustomerBankAccountCreateBodyCardObj0Metadata(
    typing_extensions.TypedDict, total=False
):
    """
    CustomerBankAccountCreateBodyCardObj0Metadata
    """


class _SerializerCustomerBankAccountCreateBodyCardObj0Metadata(pydantic.BaseModel):
    """
    Serializer for CustomerBankAccountCreateBodyCardObj0Metadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
