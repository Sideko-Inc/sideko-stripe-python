import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_data_acss_debit import (
    PaymentIntentConfirmBodyPaymentMethodDataAcssDebit,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataAcssDebit,
)
from .payment_intent_confirm_body_payment_method_data_au_becs_debit import (
    PaymentIntentConfirmBodyPaymentMethodDataAuBecsDebit,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataAuBecsDebit,
)
from .payment_intent_confirm_body_payment_method_data_bacs_debit import (
    PaymentIntentConfirmBodyPaymentMethodDataBacsDebit,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataBacsDebit,
)
from .payment_intent_confirm_body_payment_method_data_billing_details import (
    PaymentIntentConfirmBodyPaymentMethodDataBillingDetails,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataBillingDetails,
)
from .payment_intent_confirm_body_payment_method_data_boleto import (
    PaymentIntentConfirmBodyPaymentMethodDataBoleto,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataBoleto,
)
from .payment_intent_confirm_body_payment_method_data_eps import (
    PaymentIntentConfirmBodyPaymentMethodDataEps,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataEps,
)
from .payment_intent_confirm_body_payment_method_data_fpx import (
    PaymentIntentConfirmBodyPaymentMethodDataFpx,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataFpx,
)
from .payment_intent_confirm_body_payment_method_data_ideal import (
    PaymentIntentConfirmBodyPaymentMethodDataIdeal,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataIdeal,
)
from .payment_intent_confirm_body_payment_method_data_klarna import (
    PaymentIntentConfirmBodyPaymentMethodDataKlarna,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarna,
)
from .payment_intent_confirm_body_payment_method_data_metadata import (
    PaymentIntentConfirmBodyPaymentMethodDataMetadata,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataMetadata,
)
from .payment_intent_confirm_body_payment_method_data_naver_pay import (
    PaymentIntentConfirmBodyPaymentMethodDataNaverPay,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataNaverPay,
)
from .payment_intent_confirm_body_payment_method_data_nz_bank_account import (
    PaymentIntentConfirmBodyPaymentMethodDataNzBankAccount,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataNzBankAccount,
)
from .payment_intent_confirm_body_payment_method_data_p24 import (
    PaymentIntentConfirmBodyPaymentMethodDataP24,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataP24,
)
from .payment_intent_confirm_body_payment_method_data_radar_options import (
    PaymentIntentConfirmBodyPaymentMethodDataRadarOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataRadarOptions,
)
from .payment_intent_confirm_body_payment_method_data_sepa_debit import (
    PaymentIntentConfirmBodyPaymentMethodDataSepaDebit,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataSepaDebit,
)
from .payment_intent_confirm_body_payment_method_data_sofort import (
    PaymentIntentConfirmBodyPaymentMethodDataSofort,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataSofort,
)
from .payment_intent_confirm_body_payment_method_data_us_bank_account import (
    PaymentIntentConfirmBodyPaymentMethodDataUsBankAccount,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataUsBankAccount,
)


class PaymentIntentConfirmBodyPaymentMethodData(typing_extensions.TypedDict):
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataAcssDebit
    ]

    affirm: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    afterpay_clearpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    alipay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    allow_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]

    alma: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    amazon_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    au_becs_debit: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataAuBecsDebit
    ]

    bacs_debit: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataBacsDebit
    ]

    bancontact: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    billie: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    billing_details: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataBillingDetails
    ]

    blik: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    boleto: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataBoleto
    ]

    cashapp: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    customer_balance: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    eps: typing_extensions.NotRequired[PaymentIntentConfirmBodyPaymentMethodDataEps]

    fpx: typing_extensions.NotRequired[PaymentIntentConfirmBodyPaymentMethodDataFpx]

    giropay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    grabpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    ideal: typing_extensions.NotRequired[PaymentIntentConfirmBodyPaymentMethodDataIdeal]

    interac_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    kakao_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    klarna: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataKlarna
    ]

    konbini: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    kr_card: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    metadata: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataMetadata
    ]

    mobilepay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    multibanco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    naver_pay: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataNaverPay
    ]

    nz_bank_account: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataNzBankAccount
    ]

    oxxo: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    p24: typing_extensions.NotRequired[PaymentIntentConfirmBodyPaymentMethodDataP24]

    pay_by_bank: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    payco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paynow: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paypal: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    pix: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    promptpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    radar_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataRadarOptions
    ]

    revolut_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    samsung_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    satispay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    sepa_debit: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataSepaDebit
    ]

    sofort: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataSofort
    ]

    swish: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    twint: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "acss_debit",
            "affirm",
            "afterpay_clearpay",
            "alipay",
            "alma",
            "amazon_pay",
            "au_becs_debit",
            "bacs_debit",
            "bancontact",
            "billie",
            "blik",
            "boleto",
            "cashapp",
            "customer_balance",
            "eps",
            "fpx",
            "giropay",
            "grabpay",
            "ideal",
            "kakao_pay",
            "klarna",
            "konbini",
            "kr_card",
            "link",
            "mobilepay",
            "multibanco",
            "naver_pay",
            "nz_bank_account",
            "oxxo",
            "p24",
            "pay_by_bank",
            "payco",
            "paynow",
            "paypal",
            "pix",
            "promptpay",
            "revolut_pay",
            "samsung_pay",
            "satispay",
            "sepa_debit",
            "sofort",
            "swish",
            "twint",
            "us_bank_account",
            "wechat_pay",
            "zip",
        ]
    ]

    us_bank_account: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataUsBankAccount
    ]

    wechat_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    zip: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodData(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="affirm", default=None
    )
    afterpay_clearpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="afterpay_clearpay", default=None
    )
    alipay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alipay", default=None
    )
    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
    alma: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alma", default=None
    )
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataAuBecsDebit
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="bancontact", default=None
    )
    billie: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="billie", default=None
    )
    billing_details: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataBillingDetails
    ] = pydantic.Field(alias="billing_details", default=None)
    blik: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="blik", default=None
    )
    boleto: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataBoleto
    ] = pydantic.Field(alias="boleto", default=None)
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer_balance: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="customer_balance", default=None
    )
    eps: typing.Optional[_SerializerPaymentIntentConfirmBodyPaymentMethodDataEps] = (
        pydantic.Field(alias="eps", default=None)
    )
    fpx: typing.Optional[_SerializerPaymentIntentConfirmBodyPaymentMethodDataFpx] = (
        pydantic.Field(alias="fpx", default=None)
    )
    giropay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataIdeal
    ] = pydantic.Field(alias="ideal", default=None)
    interac_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="interac_present", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarna
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="konbini", default=None
    )
    kr_card: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    metadata: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    mobilepay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="multibanco", default=None
    )
    naver_pay: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataNaverPay
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataNzBankAccount
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[_SerializerPaymentIntentConfirmBodyPaymentMethodDataP24] = (
        pydantic.Field(alias="p24", default=None)
    )
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    payco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="payco", default=None
    )
    paynow: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paynow", default=None
    )
    paypal: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paypal", default=None
    )
    pix: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pix", default=None
    )
    promptpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="promptpay", default=None
    )
    radar_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataRadarOptions
    ] = pydantic.Field(alias="radar_options", default=None)
    revolut_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="revolut_pay", default=None
    )
    samsung_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="samsung_pay", default=None
    )
    satispay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="satispay", default=None
    )
    sepa_debit: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataSofort
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="swish", default=None
    )
    twint: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="twint", default=None
    )
    type_: typing_extensions.Literal[
        "acss_debit",
        "affirm",
        "afterpay_clearpay",
        "alipay",
        "alma",
        "amazon_pay",
        "au_becs_debit",
        "bacs_debit",
        "bancontact",
        "billie",
        "blik",
        "boleto",
        "cashapp",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "grabpay",
        "ideal",
        "kakao_pay",
        "klarna",
        "konbini",
        "kr_card",
        "link",
        "mobilepay",
        "multibanco",
        "naver_pay",
        "nz_bank_account",
        "oxxo",
        "p24",
        "pay_by_bank",
        "payco",
        "paynow",
        "paypal",
        "pix",
        "promptpay",
        "revolut_pay",
        "samsung_pay",
        "satispay",
        "sepa_debit",
        "sofort",
        "swish",
        "twint",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ] = pydantic.Field(
        alias="type",
    )
    us_bank_account: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
