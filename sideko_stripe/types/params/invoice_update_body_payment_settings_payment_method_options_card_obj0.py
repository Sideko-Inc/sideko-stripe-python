import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_card_obj0_installments import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0
    """

    installments: typing_extensions.NotRequired[
        InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments
    ]

    request_three_d_secure: typing_extensions.NotRequired[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    installments: typing.Optional[
        _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments
    ] = pydantic.Field(alias="installments", default=None)
    request_three_d_secure: typing.Optional[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ] = pydantic.Field(alias="request_three_d_secure", default=None)
