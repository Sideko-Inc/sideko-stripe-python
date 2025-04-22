import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options_card_obj0_installments_plan_obj0 import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
)


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments
    """

    enabled: typing_extensions.NotRequired[bool]

    plan: typing_extensions.NotRequired[
        typing.Union[
            InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0Installments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    plan: typing.Optional[
        typing.Union[
            _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ] = pydantic.Field(alias="plan", default=None)
