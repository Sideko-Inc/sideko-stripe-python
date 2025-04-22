import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_card_three_d_secure_network_options_cartes_bancaires import (
    SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
)


class SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
