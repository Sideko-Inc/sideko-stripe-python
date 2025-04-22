import pydantic
import typing
import typing_extensions

from .subscription_create_body_payment_settings_payment_method_options_card_obj0_mandate_options import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
)


class SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0
    """

    mandate_options: typing_extensions.NotRequired[
        SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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


class _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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
