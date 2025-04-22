import pydantic
import typing
import typing_extensions


class BillingCreditGrantUpdateBodyMetadata(typing_extensions.TypedDict, total=False):
    """
    Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
    """


class _SerializerBillingCreditGrantUpdateBodyMetadata(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantUpdateBodyMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
