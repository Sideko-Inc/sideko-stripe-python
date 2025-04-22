import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_acss_debit import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit,
)
from .checkout_session_create_body_payment_method_options_affirm import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAffirm,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAffirm,
)
from .checkout_session_create_body_payment_method_options_afterpay_clearpay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAfterpayClearpay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAfterpayClearpay,
)
from .checkout_session_create_body_payment_method_options_alipay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAlipay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAlipay,
)
from .checkout_session_create_body_payment_method_options_amazon_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay,
)
from .checkout_session_create_body_payment_method_options_au_becs_debit import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit,
)
from .checkout_session_create_body_payment_method_options_bacs_debit import (
    CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit,
)
from .checkout_session_create_body_payment_method_options_bancontact import (
    CheckoutSessionCreateBodyPaymentMethodOptionsBancontact,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBancontact,
)
from .checkout_session_create_body_payment_method_options_boleto import (
    CheckoutSessionCreateBodyPaymentMethodOptionsBoleto,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBoleto,
)
from .checkout_session_create_body_payment_method_options_card import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCard,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCard,
)
from .checkout_session_create_body_payment_method_options_cashapp import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCashapp,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCashapp,
)
from .checkout_session_create_body_payment_method_options_customer_balance import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance,
)
from .checkout_session_create_body_payment_method_options_eps import (
    CheckoutSessionCreateBodyPaymentMethodOptionsEps,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsEps,
)
from .checkout_session_create_body_payment_method_options_fpx import (
    CheckoutSessionCreateBodyPaymentMethodOptionsFpx,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsFpx,
)
from .checkout_session_create_body_payment_method_options_giropay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsGiropay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsGiropay,
)
from .checkout_session_create_body_payment_method_options_grabpay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsGrabpay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsGrabpay,
)
from .checkout_session_create_body_payment_method_options_ideal import (
    CheckoutSessionCreateBodyPaymentMethodOptionsIdeal,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsIdeal,
)
from .checkout_session_create_body_payment_method_options_kakao_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsKakaoPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKakaoPay,
)
from .checkout_session_create_body_payment_method_options_klarna import (
    CheckoutSessionCreateBodyPaymentMethodOptionsKlarna,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKlarna,
)
from .checkout_session_create_body_payment_method_options_konbini import (
    CheckoutSessionCreateBodyPaymentMethodOptionsKonbini,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKonbini,
)
from .checkout_session_create_body_payment_method_options_kr_card import (
    CheckoutSessionCreateBodyPaymentMethodOptionsKrCard,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKrCard,
)
from .checkout_session_create_body_payment_method_options_link import (
    CheckoutSessionCreateBodyPaymentMethodOptionsLink,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsLink,
)
from .checkout_session_create_body_payment_method_options_mobilepay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsMobilepay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsMobilepay,
)
from .checkout_session_create_body_payment_method_options_multibanco import (
    CheckoutSessionCreateBodyPaymentMethodOptionsMultibanco,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsMultibanco,
)
from .checkout_session_create_body_payment_method_options_naver_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsNaverPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsNaverPay,
)
from .checkout_session_create_body_payment_method_options_oxxo import (
    CheckoutSessionCreateBodyPaymentMethodOptionsOxxo,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsOxxo,
)
from .checkout_session_create_body_payment_method_options_p24 import (
    CheckoutSessionCreateBodyPaymentMethodOptionsP24,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsP24,
)
from .checkout_session_create_body_payment_method_options_payco import (
    CheckoutSessionCreateBodyPaymentMethodOptionsPayco,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPayco,
)
from .checkout_session_create_body_payment_method_options_paynow import (
    CheckoutSessionCreateBodyPaymentMethodOptionsPaynow,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPaynow,
)
from .checkout_session_create_body_payment_method_options_paypal import (
    CheckoutSessionCreateBodyPaymentMethodOptionsPaypal,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPaypal,
)
from .checkout_session_create_body_payment_method_options_pix import (
    CheckoutSessionCreateBodyPaymentMethodOptionsPix,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPix,
)
from .checkout_session_create_body_payment_method_options_revolut_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsRevolutPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsRevolutPay,
)
from .checkout_session_create_body_payment_method_options_samsung_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsSamsungPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSamsungPay,
)
from .checkout_session_create_body_payment_method_options_sepa_debit import (
    CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit,
)
from .checkout_session_create_body_payment_method_options_sofort import (
    CheckoutSessionCreateBodyPaymentMethodOptionsSofort,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSofort,
)
from .checkout_session_create_body_payment_method_options_swish import (
    CheckoutSessionCreateBodyPaymentMethodOptionsSwish,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSwish,
)
from .checkout_session_create_body_payment_method_options_us_bank_account import (
    CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount,
)
from .checkout_session_create_body_payment_method_options_wechat_pay import (
    CheckoutSessionCreateBodyPaymentMethodOptionsWechatPay,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsWechatPay,
)


class CheckoutSessionCreateBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment-method-specific configuration.
    """

    acss_debit: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit
    ]

    affirm: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAffirm
    ]

    afterpay_clearpay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAfterpayClearpay
    ]

    alipay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAlipay
    ]

    amazon_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay
    ]

    au_becs_debit: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit
    ]

    bacs_debit: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit
    ]

    bancontact: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsBancontact
    ]

    boleto: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsBoleto
    ]

    card: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCard
    ]

    cashapp: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCashapp
    ]

    customer_balance: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance
    ]

    eps: typing_extensions.NotRequired[CheckoutSessionCreateBodyPaymentMethodOptionsEps]

    fpx: typing_extensions.NotRequired[CheckoutSessionCreateBodyPaymentMethodOptionsFpx]

    giropay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsGiropay
    ]

    grabpay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsGrabpay
    ]

    ideal: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsIdeal
    ]

    kakao_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsKakaoPay
    ]

    klarna: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsKlarna
    ]

    konbini: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsKonbini
    ]

    kr_card: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsKrCard
    ]

    link: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsLink
    ]

    mobilepay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsMobilepay
    ]

    multibanco: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsMultibanco
    ]

    naver_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsNaverPay
    ]

    oxxo: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsOxxo
    ]

    p24: typing_extensions.NotRequired[CheckoutSessionCreateBodyPaymentMethodOptionsP24]

    pay_by_bank: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    payco: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsPayco
    ]

    paynow: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsPaynow
    ]

    paypal: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsPaypal
    ]

    pix: typing_extensions.NotRequired[CheckoutSessionCreateBodyPaymentMethodOptionsPix]

    revolut_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsRevolutPay
    ]

    samsung_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsSamsungPay
    ]

    sepa_debit: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit
    ]

    sofort: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsSofort
    ]

    swish: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsSwish
    ]

    us_bank_account: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount
    ]

    wechat_pay: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsWechatPay
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAffirm
    ] = pydantic.Field(alias="affirm", default=None)
    afterpay_clearpay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAfterpayClearpay
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAlipay
    ] = pydantic.Field(alias="alipay", default=None)
    amazon_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAmazonPay
    ] = pydantic.Field(alias="amazon_pay", default=None)
    au_becs_debit: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBancontact
    ] = pydantic.Field(alias="bancontact", default=None)
    boleto: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBoleto
    ] = pydantic.Field(alias="boleto", default=None)
    card: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCard
    ] = pydantic.Field(alias="card", default=None)
    cashapp: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCashapp
    ] = pydantic.Field(alias="cashapp", default=None)
    customer_balance: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsEps
    ] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsFpx
    ] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsGiropay
    ] = pydantic.Field(alias="giropay", default=None)
    grabpay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsGrabpay
    ] = pydantic.Field(alias="grabpay", default=None)
    ideal: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsIdeal
    ] = pydantic.Field(alias="ideal", default=None)
    kakao_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKakaoPay
    ] = pydantic.Field(alias="kakao_pay", default=None)
    klarna: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKlarna
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKonbini
    ] = pydantic.Field(alias="konbini", default=None)
    kr_card: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsKrCard
    ] = pydantic.Field(alias="kr_card", default=None)
    link: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsLink
    ] = pydantic.Field(alias="link", default=None)
    mobilepay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsMobilepay
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsMultibanco
    ] = pydantic.Field(alias="multibanco", default=None)
    naver_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsNaverPay
    ] = pydantic.Field(alias="naver_pay", default=None)
    oxxo: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsOxxo
    ] = pydantic.Field(alias="oxxo", default=None)
    p24: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsP24
    ] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    payco: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPayco
    ] = pydantic.Field(alias="payco", default=None)
    paynow: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPaynow
    ] = pydantic.Field(alias="paynow", default=None)
    paypal: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPaypal
    ] = pydantic.Field(alias="paypal", default=None)
    pix: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPix
    ] = pydantic.Field(alias="pix", default=None)
    revolut_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsRevolutPay
    ] = pydantic.Field(alias="revolut_pay", default=None)
    samsung_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSamsungPay
    ] = pydantic.Field(alias="samsung_pay", default=None)
    sepa_debit: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSofort
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSwish
    ] = pydantic.Field(alias="swish", default=None)
    us_bank_account: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsWechatPay
    ] = pydantic.Field(alias="wechat_pay", default=None)
