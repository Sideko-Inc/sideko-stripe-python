import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_card_three_d_secure_network_options_cartes_bancaires import (
    SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires,
)


class SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
