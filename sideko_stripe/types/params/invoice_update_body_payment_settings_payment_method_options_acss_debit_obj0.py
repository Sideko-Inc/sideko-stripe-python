import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_acss_debit_obj0_mandate_options import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
