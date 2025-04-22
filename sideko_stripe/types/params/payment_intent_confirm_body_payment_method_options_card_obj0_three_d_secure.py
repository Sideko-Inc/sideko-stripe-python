import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_card_obj0_three_d_secure_network_options import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure
    """

    ares_trans_status: typing_extensions.NotRequired[
        typing_extensions.Literal["A", "C", "I", "N", "R", "U", "Y"]
    ]

    cryptogram: typing_extensions.Required[str]

    electronic_commerce_indicator: typing_extensions.NotRequired[
        typing_extensions.Literal["01", "02", "05", "06", "07"]
    ]

    exemption_indicator: typing_extensions.NotRequired[
        typing_extensions.Literal["low_risk", "none"]
    ]

    network_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions
    ]

    requestor_challenge_indicator: typing_extensions.NotRequired[str]

    transaction_id: typing_extensions.Required[str]

    version: typing_extensions.Required[
        typing_extensions.Literal["1.0.2", "2.1.0", "2.2.0"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ares_trans_status: typing.Optional[
        typing_extensions.Literal["A", "C", "I", "N", "R", "U", "Y"]
    ] = pydantic.Field(alias="ares_trans_status", default=None)
    cryptogram: str = pydantic.Field(
        alias="cryptogram",
    )
    electronic_commerce_indicator: typing.Optional[
        typing_extensions.Literal["01", "02", "05", "06", "07"]
    ] = pydantic.Field(alias="electronic_commerce_indicator", default=None)
    exemption_indicator: typing.Optional[
        typing_extensions.Literal["low_risk", "none"]
    ] = pydantic.Field(alias="exemption_indicator", default=None)
    network_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptions
    ] = pydantic.Field(alias="network_options", default=None)
    requestor_challenge_indicator: typing.Optional[str] = pydantic.Field(
        alias="requestor_challenge_indicator", default=None
    )
    transaction_id: str = pydantic.Field(
        alias="transaction_id",
    )
    version: typing_extensions.Literal["1.0.2", "2.1.0", "2.2.0"] = pydantic.Field(
        alias="version",
    )
