import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_card_obj0_three_d_secure_network_options_cartes_bancaires import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
