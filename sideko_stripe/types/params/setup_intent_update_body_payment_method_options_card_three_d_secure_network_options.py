import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_card_three_d_secure_network_options_cartes_bancaires import (
    SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
)


class SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
