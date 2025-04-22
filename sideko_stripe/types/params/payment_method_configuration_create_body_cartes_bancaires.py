import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_cartes_bancaires_display_preference import (
    PaymentMethodConfigurationCreateBodyCartesBancairesDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyCartesBancairesDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyCartesBancaires(typing_extensions.TypedDict):
    """
    Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyCartesBancairesDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyCartesBancaires(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationCreateBodyCartesBancaires handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyCartesBancairesDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
