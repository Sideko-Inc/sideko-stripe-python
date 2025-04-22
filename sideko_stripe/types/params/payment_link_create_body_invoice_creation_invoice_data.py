import pydantic
import typing
import typing_extensions

from .payment_link_create_body_invoice_creation_invoice_data_custom_fields_arr0_item import (
    PaymentLinkCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
    _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
)
from .payment_link_create_body_invoice_creation_invoice_data_issuer import (
    PaymentLinkCreateBodyInvoiceCreationInvoiceDataIssuer,
    _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataIssuer,
)
from .payment_link_create_body_invoice_creation_invoice_data_metadata_obj0 import (
    PaymentLinkCreateBodyInvoiceCreationInvoiceDataMetadataObj0,
    _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataMetadataObj0,
)
from .payment_link_create_body_invoice_creation_invoice_data_rendering_options_obj0 import (
    PaymentLinkCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
    _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
)


class PaymentLinkCreateBodyInvoiceCreationInvoiceData(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyInvoiceCreationInvoiceData
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    custom_fields: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                PaymentLinkCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ]

    description: typing_extensions.NotRequired[str]

    footer: typing_extensions.NotRequired[str]

    issuer: typing_extensions.NotRequired[
        PaymentLinkCreateBodyInvoiceCreationInvoiceDataIssuer
    ]

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentLinkCreateBodyInvoiceCreationInvoiceDataMetadataObj0, str]
    ]

    rendering_options: typing_extensions.NotRequired[
        typing.Union[
            PaymentLinkCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0, str
        ]
    ]


class _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyInvoiceCreationInvoiceData handling case conversions
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
                _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="custom_fields", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    issuer: typing.Optional[
        _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataIssuer
    ] = pydantic.Field(alias="issuer", default=None)
    metadata: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataMetadataObj0, str
        ]
    ] = pydantic.Field(alias="metadata", default=None)
    rendering_options: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
            str,
        ]
    ] = pydantic.Field(alias="rendering_options", default=None)
