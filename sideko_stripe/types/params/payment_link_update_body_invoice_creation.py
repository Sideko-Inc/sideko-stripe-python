import pydantic
import typing
import typing_extensions

from .payment_link_update_body_invoice_creation_invoice_data import (
    PaymentLinkUpdateBodyInvoiceCreationInvoiceData,
    _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceData,
)


class PaymentLinkUpdateBodyInvoiceCreation(typing_extensions.TypedDict):
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    enabled: typing_extensions.Required[bool]

    invoice_data: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyInvoiceCreationInvoiceData
    ]


class _SerializerPaymentLinkUpdateBodyInvoiceCreation(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyInvoiceCreation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    invoice_data: typing.Optional[
        _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceData
    ] = pydantic.Field(alias="invoice_data", default=None)
