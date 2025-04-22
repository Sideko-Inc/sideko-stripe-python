import pydantic
import typing
import typing_extensions

from .invoice_preview_body_customer_details_address_obj0 import (
    InvoicePreviewBodyCustomerDetailsAddressObj0,
    _SerializerInvoicePreviewBodyCustomerDetailsAddressObj0,
)
from .invoice_preview_body_customer_details_shipping_obj0 import (
    InvoicePreviewBodyCustomerDetailsShippingObj0,
    _SerializerInvoicePreviewBodyCustomerDetailsShippingObj0,
)
from .invoice_preview_body_customer_details_tax import (
    InvoicePreviewBodyCustomerDetailsTax,
    _SerializerInvoicePreviewBodyCustomerDetailsTax,
)
from .invoice_preview_body_customer_details_tax_ids_item import (
    InvoicePreviewBodyCustomerDetailsTaxIdsItem,
    _SerializerInvoicePreviewBodyCustomerDetailsTaxIdsItem,
)


class InvoicePreviewBodyCustomerDetails(typing_extensions.TypedDict):
    """
    Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
    """

    address: typing_extensions.NotRequired[
        typing.Union[InvoicePreviewBodyCustomerDetailsAddressObj0, str]
    ]

    shipping: typing_extensions.NotRequired[
        typing.Union[InvoicePreviewBodyCustomerDetailsShippingObj0, str]
    ]

    tax: typing_extensions.NotRequired[InvoicePreviewBodyCustomerDetailsTax]

    tax_exempt: typing_extensions.NotRequired[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ]

    tax_ids: typing_extensions.NotRequired[
        typing.List[InvoicePreviewBodyCustomerDetailsTaxIdsItem]
    ]


class _SerializerInvoicePreviewBodyCustomerDetails(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyCustomerDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[_SerializerInvoicePreviewBodyCustomerDetailsAddressObj0, str]
    ] = pydantic.Field(alias="address", default=None)
    shipping: typing.Optional[
        typing.Union[_SerializerInvoicePreviewBodyCustomerDetailsShippingObj0, str]
    ] = pydantic.Field(alias="shipping", default=None)
    tax: typing.Optional[_SerializerInvoicePreviewBodyCustomerDetailsTax] = (
        pydantic.Field(alias="tax", default=None)
    )
    tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="tax_exempt", default=None)
    tax_ids: typing.Optional[
        typing.List[_SerializerInvoicePreviewBodyCustomerDetailsTaxIdsItem]
    ] = pydantic.Field(alias="tax_ids", default=None)
