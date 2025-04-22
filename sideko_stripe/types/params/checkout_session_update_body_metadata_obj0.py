import pydantic
import typing
import typing_extensions


class CheckoutSessionUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    CheckoutSessionUpdateBodyMetadataObj0
    """


class _SerializerCheckoutSessionUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
