import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_amazon_pay_display_preference import (
    PaymentMethodConfigurationCreateBodyAmazonPayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAmazonPayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAmazonPay(typing_extensions.TypedDict):
    """
    Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAmazonPayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAmazonPay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAmazonPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAmazonPayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
