import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_card_three_d_secure_network_options import (
    SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions,
)


class SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure(
    typing_extensions.TypedDict
):
    """
    SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure
    """

    ares_trans_status: typing_extensions.NotRequired[
        typing_extensions.Literal["A", "C", "I", "N", "R", "U", "Y"]
    ]

    cryptogram: typing_extensions.NotRequired[str]

    electronic_commerce_indicator: typing_extensions.NotRequired[
        typing_extensions.Literal["01", "02", "05", "06", "07"]
    ]

    network_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions
    ]

    requestor_challenge_indicator: typing_extensions.NotRequired[str]

    transaction_id: typing_extensions.NotRequired[str]

    version: typing_extensions.NotRequired[
        typing_extensions.Literal["1.0.2", "2.1.0", "2.2.0"]
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ares_trans_status: typing.Optional[
        typing_extensions.Literal["A", "C", "I", "N", "R", "U", "Y"]
    ] = pydantic.Field(alias="ares_trans_status", default=None)
    cryptogram: typing.Optional[str] = pydantic.Field(alias="cryptogram", default=None)
    electronic_commerce_indicator: typing.Optional[
        typing_extensions.Literal["01", "02", "05", "06", "07"]
    ] = pydantic.Field(alias="electronic_commerce_indicator", default=None)
    network_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecureNetworkOptions
    ] = pydantic.Field(alias="network_options", default=None)
    requestor_challenge_indicator: typing.Optional[str] = pydantic.Field(
        alias="requestor_challenge_indicator", default=None
    )
    transaction_id: typing.Optional[str] = pydantic.Field(
        alias="transaction_id", default=None
    )
    version: typing.Optional[typing_extensions.Literal["1.0.2", "2.1.0", "2.2.0"]] = (
        pydantic.Field(alias="version", default=None)
    )
