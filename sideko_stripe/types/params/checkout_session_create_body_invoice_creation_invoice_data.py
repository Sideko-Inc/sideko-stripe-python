import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_invoice_creation_invoice_data_custom_fields_arr0_item import (
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
    _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item,
)
from .checkout_session_create_body_invoice_creation_invoice_data_issuer import (
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataIssuer,
    _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataIssuer,
)
from .checkout_session_create_body_invoice_creation_invoice_data_metadata import (
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata,
    _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata,
)
from .checkout_session_create_body_invoice_creation_invoice_data_rendering_options_obj0 import (
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
    _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
)


class CheckoutSessionCreateBodyInvoiceCreationInvoiceData(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyInvoiceCreationInvoiceData
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    custom_fields: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                CheckoutSessionCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ]

    description: typing_extensions.NotRequired[str]

    footer: typing_extensions.NotRequired[str]

    issuer: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyInvoiceCreationInvoiceDataIssuer
    ]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata
    ]

    rendering_options: typing_extensions.NotRequired[
        typing.Union[
            CheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0, str
        ]
    ]


class _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceData(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyInvoiceCreationInvoiceData handling case conversions
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
                _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataCustomFieldsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="custom_fields", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    issuer: typing.Optional[
        _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataIssuer
    ] = pydantic.Field(alias="issuer", default=None)
    metadata: typing.Optional[
        _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    rendering_options: typing.Optional[
        typing.Union[
            _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0,
            str,
        ]
    ] = pydantic.Field(alias="rendering_options", default=None)
