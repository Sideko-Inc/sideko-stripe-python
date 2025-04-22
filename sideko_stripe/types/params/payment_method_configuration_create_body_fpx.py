import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_fpx_display_preference import (
    PaymentMethodConfigurationCreateBodyFpxDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyFpxDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyFpx(typing_extensions.TypedDict):
    """
    Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyFpxDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyFpx(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyFpx handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyFpxDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
