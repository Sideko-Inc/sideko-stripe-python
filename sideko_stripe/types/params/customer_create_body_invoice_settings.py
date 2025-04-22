import pydantic
import typing
import typing_extensions

from .customer_create_body_invoice_settings_custom_fields_arr0_item import (
    CustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item,
    _SerializerCustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item,
)
from .customer_create_body_invoice_settings_rendering_options_obj0 import (
    CustomerCreateBodyInvoiceSettingsRenderingOptionsObj0,
    _SerializerCustomerCreateBodyInvoiceSettingsRenderingOptionsObj0,
)


class CustomerCreateBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    Default invoice settings for this customer.
    """

    custom_fields: typing_extensions.NotRequired[
        typing.Union[
            typing.List[CustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item], str
        ]
    ]

    default_payment_method: typing_extensions.NotRequired[str]

    footer: typing_extensions.NotRequired[str]

    rendering_options: typing_extensions.NotRequired[
        typing.Union[CustomerCreateBodyInvoiceSettingsRenderingOptionsObj0, str]
    ]


class _SerializerCustomerCreateBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_fields: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerCustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="custom_fields", default=None)
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    rendering_options: typing.Optional[
        typing.Union[
            _SerializerCustomerCreateBodyInvoiceSettingsRenderingOptionsObj0, str
        ]
    ] = pydantic.Field(alias="rendering_options", default=None)
