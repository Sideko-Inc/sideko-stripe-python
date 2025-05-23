import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_giropay_display_preference import (
    PaymentMethodConfigurationCreateBodyGiropayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyGiropayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyGiropay(typing_extensions.TypedDict):
    """
    giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyGiropayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyGiropay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyGiropay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyGiropayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
