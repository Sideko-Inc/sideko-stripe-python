import pydantic
import typing
import typing_extensions


class InvoicePreviewBodyCustomerDetailsTax(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyCustomerDetailsTax
    """

    ip_address: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerInvoicePreviewBodyCustomerDetailsTax(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyCustomerDetailsTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ip_address: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="ip_address", default=None
    )
