import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_card_mandate_options import (
    SetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions,
)
from .setup_intent_update_body_payment_method_options_card_three_d_secure import (
    SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecure,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecure,
)


class SetupIntentUpdateBodyPaymentMethodOptionsCard(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsCard
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions
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
        SetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecure
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCard(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions
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
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
