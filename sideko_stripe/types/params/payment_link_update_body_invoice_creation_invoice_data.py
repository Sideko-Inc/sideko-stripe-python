import pydantic
import typing
import typing_extensions

from .payment_link_update_body_invoice_creation_invoice_data_custom_fields_arr0_item import (
    PaymentLinkUpdateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
    _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
)
from .payment_link_update_body_invoice_creation_invoice_data_issuer import (
    PaymentLinkUpdateBodyInvoiceCreationInvoiceDataIssuer,
    _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataIssuer,
)
from .payment_link_update_body_invoice_creation_invoice_data_metadata_obj0 import (
    PaymentLinkUpdateBodyInvoiceCreationInvoiceDataMetadataObj0,
    _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataMetadataObj0,
)
from .payment_link_update_body_invoice_creation_invoice_data_rendering_options_obj0 import (
    PaymentLinkUpdateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
    _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
)


class PaymentLinkUpdateBodyInvoiceCreationInvoiceData(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyInvoiceCreationInvoiceData
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    custom_fields: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                PaymentLinkUpdateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ]

    description: typing_extensions.NotRequired[str]

    footer: typing_extensions.NotRequired[str]

    issuer: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyInvoiceCreationInvoiceDataIssuer
    ]

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyInvoiceCreationInvoiceDataMetadataObj0, str]
    ]

    rendering_options: typing_extensions.NotRequired[
        typing.Union[
            PaymentLinkUpdateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0, str
        ]
    ]


class _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyInvoiceCreationInvoiceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    custom_fields: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="custom_fields", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    issuer: typing.Optional[
        _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataIssuer
    ] = pydantic.Field(alias="issuer", default=None)
    metadata: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataMetadataObj0, str
        ]
    ] = pydantic.Field(alias="metadata", default=None)
    rendering_options: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkUpdateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
            str,
        ]
    ] = pydantic.Field(alias="rendering_options", default=None)
