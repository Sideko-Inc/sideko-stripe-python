import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_grabpay_display_preference import (
    PaymentMethodConfigurationUpdateBodyGrabpayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyGrabpayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyGrabpay(typing_extensions.TypedDict):
    """
    GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyGrabpayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyGrabpay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyGrabpay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyGrabpayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
