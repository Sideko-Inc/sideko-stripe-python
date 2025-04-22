import pydantic
import typing
import typing_extensions

from .invoice_update_body_payment_settings_payment_method_options import (
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptions,
    _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptions,
)


class InvoiceUpdateBodyPaymentSettings(typing_extensions.TypedDict):
    """
    Configuration settings for the PaymentIntent that is generated when the invoice is finalized.
    """

    default_mandate: typing_extensions.NotRequired[typing.Union[str, str]]

    payment_method_options: typing_extensions.NotRequired[
        InvoiceUpdateBodyPaymentSettingsPaymentMethodOptions
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


class _SerializerInvoiceUpdateBodyPaymentSettings(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyPaymentSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_mandate: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="default_mandate", default=None
    )
    payment_method_options: typing.Optional[
        _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptions
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
