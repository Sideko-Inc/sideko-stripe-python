import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_paynow_display_preference import (
    PaymentMethodConfigurationCreateBodyPaynowDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyPaynowDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyPaynow(typing_extensions.TypedDict):
    """
    PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyPaynowDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyPaynow(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyPaynow handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyPaynowDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
