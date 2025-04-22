import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_card_mandate_options import (
    SetupIntentCreateBodyPaymentMethodOptionsCardMandateOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardMandateOptions,
)
from .setup_intent_create_body_payment_method_options_card_three_d_secure import (
    SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure,
)


class SetupIntentCreateBodyPaymentMethodOptionsCard(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodOptionsCard
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsCardMandateOptions
    ]

    network: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ]

    request_three_d_secure: typing_extensions.NotRequired[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ]

    three_d_secure: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsCard(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    network: typing.Optional[
        typing_extensions.Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ] = pydantic.Field(alias="network", default=None)
    request_three_d_secure: typing.Optional[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ] = pydantic.Field(alias="request_three_d_secure", default=None)
    three_d_secure: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsCardThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
