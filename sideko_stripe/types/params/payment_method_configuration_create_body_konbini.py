import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_konbini_display_preference import (
    PaymentMethodConfigurationCreateBodyKonbiniDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyKonbiniDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyKonbini(typing_extensions.TypedDict):
    """
    Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyKonbiniDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyKonbini(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyKonbini handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyKonbiniDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
