import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_alma_display_preference import (
    PaymentMethodConfigurationCreateBodyAlmaDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAlmaDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAlma(typing_extensions.TypedDict):
    """
    Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAlmaDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAlma(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAlma handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAlmaDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
