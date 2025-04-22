import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_ideal_display_preference import (
    PaymentMethodConfigurationUpdateBodyIdealDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyIdealDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyIdeal(typing_extensions.TypedDict):
    """
    iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyIdealDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyIdeal(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyIdeal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyIdealDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
