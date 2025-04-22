import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_payment_settings_payment_method_options_card_obj0_mandate_options import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions,
)


class CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0
    """

    mandate_options: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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


class _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
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
