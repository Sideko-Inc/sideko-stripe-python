import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_konbini_display_preference import (
    PaymentMethodConfigurationUpdateBodyKonbiniDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyKonbiniDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyKonbini(typing_extensions.TypedDict):
    """
    Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyKonbiniDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyKonbini(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyKonbini handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyKonbiniDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
