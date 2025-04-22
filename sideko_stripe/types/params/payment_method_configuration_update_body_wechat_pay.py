import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_wechat_pay_display_preference import (
    PaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyWechatPay(typing_extensions.TypedDict):
    """
    WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyWechatPay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyWechatPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
