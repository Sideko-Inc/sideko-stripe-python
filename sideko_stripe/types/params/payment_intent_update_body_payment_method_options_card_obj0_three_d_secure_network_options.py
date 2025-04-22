import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_card_obj0_three_d_secure_network_options_cartes_bancaires import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires,
)


class PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions
    """

    cartes_bancaires: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cartes_bancaires: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
