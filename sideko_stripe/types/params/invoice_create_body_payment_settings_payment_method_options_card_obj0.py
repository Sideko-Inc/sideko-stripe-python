import pydantic
import typing
import typing_extensions

from .invoice_create_body_payment_settings_payment_method_options_card_obj0_installments import (
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments,
    _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments,
)


class InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    typing_extensions.TypedDict
):
    """
    InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0
    """

    installments: typing_extensions.NotRequired[
        InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments
    ]

    request_three_d_secure: typing_extensions.NotRequired[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ]


class _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    installments: typing.Optional[
        _SerializerInvoiceCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments
    ] = pydantic.Field(alias="installments", default=None)
    request_three_d_secure: typing.Optional[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ] = pydantic.Field(alias="request_three_d_secure", default=None)
