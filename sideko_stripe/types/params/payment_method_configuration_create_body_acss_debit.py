import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_acss_debit_display_preference import (
    PaymentMethodConfigurationCreateBodyAcssDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAcssDebitDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAcssDebit(typing_extensions.TypedDict):
    """
    Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAcssDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAcssDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAcssDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAcssDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
