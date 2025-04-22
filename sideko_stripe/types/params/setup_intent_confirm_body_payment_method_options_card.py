import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_card_mandate_options import (
    SetupIntentConfirmBodyPaymentMethodOptionsCardMandateOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardMandateOptions,
)
from .setup_intent_confirm_body_payment_method_options_card_three_d_secure import (
    SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecure,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecure,
)


class SetupIntentConfirmBodyPaymentMethodOptionsCard(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsCard
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsCardMandateOptions
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
        SetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecure
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCard(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardMandateOptions
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
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCardThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
