import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_card_obj0_installments import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments,
)
from .payment_intent_create_body_payment_method_options_card_obj0_mandate_options import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0MandateOptions,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0MandateOptions,
)
from .payment_intent_create_body_payment_method_options_card_obj0_three_d_secure import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecure,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecure,
)


class PaymentIntentCreateBodyPaymentMethodOptionsCardObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]

    cvc_token: typing_extensions.NotRequired[str]

    installments: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments
    ]

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCardObj0MandateOptions
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

    request_extended_authorization: typing_extensions.NotRequired[
        typing_extensions.Literal["if_available", "never"]
    ]

    request_incremental_authorization: typing_extensions.NotRequired[
        typing_extensions.Literal["if_available", "never"]
    ]

    request_multicapture: typing_extensions.NotRequired[
        typing_extensions.Literal["if_available", "never"]
    ]

    request_overcapture: typing_extensions.NotRequired[
        typing_extensions.Literal["if_available", "never"]
    ]

    request_three_d_secure: typing_extensions.NotRequired[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ]

    require_cvc_recollection: typing_extensions.NotRequired[bool]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    statement_descriptor_suffix_kana: typing_extensions.NotRequired[
        typing.Union[str, str]
    ]

    statement_descriptor_suffix_kanji: typing_extensions.NotRequired[
        typing.Union[str, str]
    ]

    three_d_secure: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecure
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
    cvc_token: typing.Optional[str] = pydantic.Field(alias="cvc_token", default=None)
    installments: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments
    ] = pydantic.Field(alias="installments", default=None)
    mandate_options: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0MandateOptions
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
    request_extended_authorization: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_extended_authorization", default=None)
    request_incremental_authorization: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_incremental_authorization", default=None)
    request_multicapture: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_multicapture", default=None)
    request_overcapture: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_overcapture", default=None)
    request_three_d_secure: typing.Optional[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ] = pydantic.Field(alias="request_three_d_secure", default=None)
    require_cvc_recollection: typing.Optional[bool] = pydantic.Field(
        alias="require_cvc_recollection", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    statement_descriptor_suffix_kana: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="statement_descriptor_suffix_kana", default=None)
    )
    statement_descriptor_suffix_kanji: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="statement_descriptor_suffix_kanji", default=None)
    )
    three_d_secure: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0ThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
