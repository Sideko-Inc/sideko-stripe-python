import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_alma_display_preference import (
    PaymentMethodConfigurationUpdateBodyAlmaDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyAlmaDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyAlma(typing_extensions.TypedDict):
    """
    Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAlmaDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyAlma(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyAlma handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAlmaDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
