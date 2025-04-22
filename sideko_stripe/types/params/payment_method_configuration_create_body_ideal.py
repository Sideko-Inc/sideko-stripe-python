import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_ideal_display_preference import (
    PaymentMethodConfigurationCreateBodyIdealDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyIdealDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyIdeal(typing_extensions.TypedDict):
    """
    iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyIdealDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyIdeal(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyIdeal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyIdealDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
