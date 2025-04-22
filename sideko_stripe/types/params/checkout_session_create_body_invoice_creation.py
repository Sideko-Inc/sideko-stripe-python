import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_invoice_creation_invoice_data import (
    CheckoutSessionCreateBodyInvoiceCreationInvoiceData,
    _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceData,
)


class CheckoutSessionCreateBodyInvoiceCreation(typing_extensions.TypedDict):
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    enabled: typing_extensions.Required[bool]

    invoice_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyInvoiceCreationInvoiceData
    ]


class _SerializerCheckoutSessionCreateBodyInvoiceCreation(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyInvoiceCreation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    invoice_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceData
    ] = pydantic.Field(alias="invoice_data", default=None)
