import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_alipay_display_preference import (
    PaymentMethodConfigurationUpdateBodyAlipayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyAlipayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyAlipay(typing_extensions.TypedDict):
    """
    Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAlipayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyAlipay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyAlipay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAlipayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
