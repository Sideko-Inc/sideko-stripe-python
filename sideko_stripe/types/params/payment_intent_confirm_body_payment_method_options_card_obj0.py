import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_card_obj0_installments import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments,
)
from .payment_intent_confirm_body_payment_method_options_card_obj0_mandate_options import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0MandateOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0MandateOptions,
)
from .payment_intent_confirm_body_payment_method_options_card_obj0_three_d_secure import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]

    cvc_token: typing_extensions.NotRequired[str]

    installments: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments
    ]

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0MandateOptions
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
        PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0 handling case conversions
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
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments
    ] = pydantic.Field(alias="installments", default=None)
    mandate_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0MandateOptions
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
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
