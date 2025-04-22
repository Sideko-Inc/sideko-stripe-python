import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata
    """


class _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
