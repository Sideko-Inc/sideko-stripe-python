import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_acss_debit_obj0_mandate_options import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
