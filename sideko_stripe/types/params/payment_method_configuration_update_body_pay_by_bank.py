import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_pay_by_bank_display_preference import (
    PaymentMethodConfigurationUpdateBodyPayByBankDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyPayByBankDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyPayByBank(typing_extensions.TypedDict):
    """
    Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyPayByBankDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyPayByBank(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyPayByBank handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyPayByBankDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
