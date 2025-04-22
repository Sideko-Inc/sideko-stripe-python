import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_card_obj0_mandate_options import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0
    """

    mandate_options: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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
