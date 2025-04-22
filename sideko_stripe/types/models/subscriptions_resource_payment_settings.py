import pydantic
import typing
import typing_extensions

from .subscriptions_resource_payment_method_options import (
    SubscriptionsResourcePaymentMethodOptions,
)


class SubscriptionsResourcePaymentSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_method_options: typing.Optional[
        SubscriptionsResourcePaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[
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
        ]
    ] = pydantic.Field(alias="payment_method_types", default=None)
    """
    The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice’s default payment method, the subscription’s default payment method, the customer’s default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
    """
    save_default_payment_method: typing.Optional[
        typing_extensions.Literal["off", "on_subscription"]
    ] = pydantic.Field(alias="save_default_payment_method", default=None)
    """
    Configure whether Stripe updates `subscription.default_payment_method` when payment succeeds. Defaults to `off`.
    """
