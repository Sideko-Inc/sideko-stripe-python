import pydantic
import typing
import typing_extensions

from .payment_link_create_body_invoice_creation_invoice_data import (
    PaymentLinkCreateBodyInvoiceCreationInvoiceData,
    _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceData,
)


class PaymentLinkCreateBodyInvoiceCreation(typing_extensions.TypedDict):
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    enabled: typing_extensions.Required[bool]

    invoice_data: typing_extensions.NotRequired[
        PaymentLinkCreateBodyInvoiceCreationInvoiceData
    ]


class _SerializerPaymentLinkCreateBodyInvoiceCreation(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyInvoiceCreation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    invoice_data: typing.Optional[
        _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceData
    ] = pydantic.Field(alias="invoice_data", default=None)
