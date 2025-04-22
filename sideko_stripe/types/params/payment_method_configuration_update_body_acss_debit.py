import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_acss_debit_display_preference import (
    PaymentMethodConfigurationUpdateBodyAcssDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyAcssDebitDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyAcssDebit(typing_extensions.TypedDict):
    """
    Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAcssDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyAcssDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyAcssDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAcssDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
