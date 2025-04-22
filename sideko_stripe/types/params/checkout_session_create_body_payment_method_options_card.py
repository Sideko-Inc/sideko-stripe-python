import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_card_installments import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCardInstallments,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCardInstallments,
)
from .checkout_session_create_body_payment_method_options_card_restrictions import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsCard(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsCard
    """

    installments: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCardInstallments
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

    restrictions: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]

    statement_descriptor_suffix_kana: typing_extensions.NotRequired[str]

    statement_descriptor_suffix_kanji: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCard(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    installments: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCardInstallments
    ] = pydantic.Field(alias="installments", default=None)
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
    restrictions: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions
    ] = pydantic.Field(alias="restrictions", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    statement_descriptor_suffix_kana: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix_kana", default=None
    )
    statement_descriptor_suffix_kanji: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix_kanji", default=None
    )
