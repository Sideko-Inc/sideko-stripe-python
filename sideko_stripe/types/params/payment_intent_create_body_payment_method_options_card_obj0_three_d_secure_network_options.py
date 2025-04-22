import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_card_obj0_three_d_secure_network_options_cartes_bancaires import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
)


class PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
