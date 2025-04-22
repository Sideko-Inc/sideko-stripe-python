import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_payment_settings_payment_method_options import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions,
)


class CustomerSubscriptionModifyBodyPaymentSettings(typing_extensions.TypedDict):
    """
    Payment settings to pass to invoices created by the subscription.
    """

    payment_method_options: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions
    ]

    payment_method_types: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "ach_credit_transfer",
                    "ach_debit",
                    "acss_debit",
                    "amazon_pay",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "jp_credit_transfer",
                    "kakao_pay",
                    "klarna",
                    "konbini",
                    "kr_card",
                    "link",
                    "multibanco",
                    "naver_pay",
                    "nz_bank_account",
                    "p24",
                    "payco",
                    "paynow",
                    "paypal",
                    "promptpay",
                    "revolut_pay",
                    "sepa_credit_transfer",
                    "sepa_debit",
                    "sofort",
                    "swish",
                    "us_bank_account",
                    "wechat_pay",
                ]
            ],
            str,
        ]
    ]

    save_default_payment_method: typing_extensions.NotRequired[
        typing_extensions.Literal["off", "on_subscription"]
    ]


class _SerializerCustomerSubscriptionModifyBodyPaymentSettings(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyPaymentSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payment_method_options: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "ach_credit_transfer",
                    "ach_debit",
                    "acss_debit",
                    "amazon_pay",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "jp_credit_transfer",
                    "kakao_pay",
                    "klarna",
                    "konbini",
                    "kr_card",
                    "link",
                    "multibanco",
                    "naver_pay",
                    "nz_bank_account",
                    "p24",
                    "payco",
                    "paynow",
                    "paypal",
                    "promptpay",
                    "revolut_pay",
                    "sepa_credit_transfer",
                    "sepa_debit",
                    "sofort",
                    "swish",
                    "us_bank_account",
                    "wechat_pay",
                ]
            ],
            str,
        ]
    ] = pydantic.Field(alias="payment_method_types", default=None)
    save_default_payment_method: typing.Optional[
        typing_extensions.Literal["off", "on_subscription"]
    ] = pydantic.Field(alias="save_default_payment_method", default=None)
