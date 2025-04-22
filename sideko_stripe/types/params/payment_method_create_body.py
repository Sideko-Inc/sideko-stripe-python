import pydantic
import typing
import typing_extensions

from .payment_method_create_body_acss_debit import (
    PaymentMethodCreateBodyAcssDebit,
    _SerializerPaymentMethodCreateBodyAcssDebit,
)
from .payment_method_create_body_au_becs_debit import (
    PaymentMethodCreateBodyAuBecsDebit,
    _SerializerPaymentMethodCreateBodyAuBecsDebit,
)
from .payment_method_create_body_bacs_debit import (
    PaymentMethodCreateBodyBacsDebit,
    _SerializerPaymentMethodCreateBodyBacsDebit,
)
from .payment_method_create_body_billing_details import (
    PaymentMethodCreateBodyBillingDetails,
    _SerializerPaymentMethodCreateBodyBillingDetails,
)
from .payment_method_create_body_boleto import (
    PaymentMethodCreateBodyBoleto,
    _SerializerPaymentMethodCreateBodyBoleto,
)
from .payment_method_create_body_card_obj0 import (
    PaymentMethodCreateBodyCardObj0,
    _SerializerPaymentMethodCreateBodyCardObj0,
)
from .payment_method_create_body_card_obj1 import (
    PaymentMethodCreateBodyCardObj1,
    _SerializerPaymentMethodCreateBodyCardObj1,
)
from .payment_method_create_body_eps import (
    PaymentMethodCreateBodyEps,
    _SerializerPaymentMethodCreateBodyEps,
)
from .payment_method_create_body_fpx import (
    PaymentMethodCreateBodyFpx,
    _SerializerPaymentMethodCreateBodyFpx,
)
from .payment_method_create_body_ideal import (
    PaymentMethodCreateBodyIdeal,
    _SerializerPaymentMethodCreateBodyIdeal,
)
from .payment_method_create_body_klarna import (
    PaymentMethodCreateBodyKlarna,
    _SerializerPaymentMethodCreateBodyKlarna,
)
from .payment_method_create_body_metadata import (
    PaymentMethodCreateBodyMetadata,
    _SerializerPaymentMethodCreateBodyMetadata,
)
from .payment_method_create_body_naver_pay import (
    PaymentMethodCreateBodyNaverPay,
    _SerializerPaymentMethodCreateBodyNaverPay,
)
from .payment_method_create_body_nz_bank_account import (
    PaymentMethodCreateBodyNzBankAccount,
    _SerializerPaymentMethodCreateBodyNzBankAccount,
)
from .payment_method_create_body_p24 import (
    PaymentMethodCreateBodyP24,
    _SerializerPaymentMethodCreateBodyP24,
)
from .payment_method_create_body_radar_options import (
    PaymentMethodCreateBodyRadarOptions,
    _SerializerPaymentMethodCreateBodyRadarOptions,
)
from .payment_method_create_body_sepa_debit import (
    PaymentMethodCreateBodySepaDebit,
    _SerializerPaymentMethodCreateBodySepaDebit,
)
from .payment_method_create_body_sofort import (
    PaymentMethodCreateBodySofort,
    _SerializerPaymentMethodCreateBodySofort,
)
from .payment_method_create_body_us_bank_account import (
    PaymentMethodCreateBodyUsBankAccount,
    _SerializerPaymentMethodCreateBodyUsBankAccount,
)


class PaymentMethodCreateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodCreateBody
    """

    acss_debit: typing_extensions.NotRequired[PaymentMethodCreateBodyAcssDebit]
    """
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
    """

    affirm: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
    """

    afterpay_clearpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
    """

    alipay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
    """

    allow_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    """

    alma: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.
    """

    amazon_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.
    """

    au_becs_debit: typing_extensions.NotRequired[PaymentMethodCreateBodyAuBecsDebit]
    """
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    """

    bacs_debit: typing_extensions.NotRequired[PaymentMethodCreateBodyBacsDebit]
    """
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    """

    bancontact: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
    """

    billie: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `billie` PaymentMethod, this hash contains details about the billie payment method.
    """

    billing_details: typing_extensions.NotRequired[
        PaymentMethodCreateBodyBillingDetails
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """

    blik: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
    """

    boleto: typing_extensions.NotRequired[PaymentMethodCreateBodyBoleto]
    """
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    """

    card: typing_extensions.NotRequired[
        typing.Union[PaymentMethodCreateBodyCardObj0, PaymentMethodCreateBodyCardObj1]
    ]
    """
    If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly.
    """

    cashapp: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The `Customer` to whom the original PaymentMethod is attached.
    """

    customer_balance: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
    """

    eps: typing_extensions.NotRequired[PaymentMethodCreateBodyEps]
    """
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fpx: typing_extensions.NotRequired[PaymentMethodCreateBodyFpx]
    """
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    """

    giropay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
    """

    grabpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
    """

    ideal: typing_extensions.NotRequired[PaymentMethodCreateBodyIdeal]
    """
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    """

    interac_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
    """

    kakao_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.
    """

    klarna: typing_extensions.NotRequired[PaymentMethodCreateBodyKlarna]
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    """

    konbini: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
    """

    kr_card: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.
    """

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    """

    metadata: typing_extensions.NotRequired[PaymentMethodCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    mobilepay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.
    """

    multibanco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.
    """

    naver_pay: typing_extensions.NotRequired[PaymentMethodCreateBodyNaverPay]
    """
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    """

    nz_bank_account: typing_extensions.NotRequired[PaymentMethodCreateBodyNzBankAccount]
    """
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    """

    oxxo: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
    """

    p24: typing_extensions.NotRequired[PaymentMethodCreateBodyP24]
    """
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
    """

    pay_by_bank: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    """

    payco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    The PaymentMethod to share.
    """

    paynow: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
    """

    paypal: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
    """

    pix: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
    """

    promptpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
    """

    radar_options: typing_extensions.NotRequired[PaymentMethodCreateBodyRadarOptions]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """

    revolut_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `Revolut Pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
    """

    samsung_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.
    """

    satispay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `satispay` PaymentMethod, this hash contains details about the satispay payment method.
    """

    sepa_debit: typing_extensions.NotRequired[PaymentMethodCreateBodySepaDebit]
    """
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    """

    sofort: typing_extensions.NotRequired[PaymentMethodCreateBodySofort]
    """
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    """

    swish: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.
    """

    twint: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.
    """

    type_: typing_extensions.NotRequired[
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
            "card",
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
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """

    us_bank_account: typing_extensions.NotRequired[PaymentMethodCreateBodyUsBankAccount]
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """

    wechat_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
    """

    zip: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
    """


class _SerializerPaymentMethodCreateBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    acss_debit: typing.Optional[_SerializerPaymentMethodCreateBodyAcssDebit] = (
        pydantic.Field(alias="acss_debit", default=None)
    )
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
    au_becs_debit: typing.Optional[_SerializerPaymentMethodCreateBodyAuBecsDebit] = (
        pydantic.Field(alias="au_becs_debit", default=None)
    )
    bacs_debit: typing.Optional[_SerializerPaymentMethodCreateBodyBacsDebit] = (
        pydantic.Field(alias="bacs_debit", default=None)
    )
    bancontact: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="bancontact", default=None
    )
    billie: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="billie", default=None
    )
    billing_details: typing.Optional[
        _SerializerPaymentMethodCreateBodyBillingDetails
    ] = pydantic.Field(alias="billing_details", default=None)
    blik: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="blik", default=None
    )
    boleto: typing.Optional[_SerializerPaymentMethodCreateBodyBoleto] = pydantic.Field(
        alias="boleto", default=None
    )
    card: typing.Optional[
        typing.Union[
            _SerializerPaymentMethodCreateBodyCardObj0,
            _SerializerPaymentMethodCreateBodyCardObj1,
        ]
    ] = pydantic.Field(alias="card", default=None)
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    customer_balance: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="customer_balance", default=None
    )
    eps: typing.Optional[_SerializerPaymentMethodCreateBodyEps] = pydantic.Field(
        alias="eps", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fpx: typing.Optional[_SerializerPaymentMethodCreateBodyFpx] = pydantic.Field(
        alias="fpx", default=None
    )
    giropay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional[_SerializerPaymentMethodCreateBodyIdeal] = pydantic.Field(
        alias="ideal", default=None
    )
    interac_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="interac_present", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[_SerializerPaymentMethodCreateBodyKlarna] = pydantic.Field(
        alias="klarna", default=None
    )
    konbini: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="konbini", default=None
    )
    kr_card: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    metadata: typing.Optional[_SerializerPaymentMethodCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    mobilepay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="multibanco", default=None
    )
    naver_pay: typing.Optional[_SerializerPaymentMethodCreateBodyNaverPay] = (
        pydantic.Field(alias="naver_pay", default=None)
    )
    nz_bank_account: typing.Optional[
        _SerializerPaymentMethodCreateBodyNzBankAccount
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[_SerializerPaymentMethodCreateBodyP24] = pydantic.Field(
        alias="p24", default=None
    )
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    payco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="payco", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
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
    radar_options: typing.Optional[_SerializerPaymentMethodCreateBodyRadarOptions] = (
        pydantic.Field(alias="radar_options", default=None)
    )
    revolut_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="revolut_pay", default=None
    )
    samsung_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="samsung_pay", default=None
    )
    satispay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="satispay", default=None
    )
    sepa_debit: typing.Optional[_SerializerPaymentMethodCreateBodySepaDebit] = (
        pydantic.Field(alias="sepa_debit", default=None)
    )
    sofort: typing.Optional[_SerializerPaymentMethodCreateBodySofort] = pydantic.Field(
        alias="sofort", default=None
    )
    swish: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="swish", default=None
    )
    twint: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="twint", default=None
    )
    type_: typing.Optional[
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
            "card",
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
    ] = pydantic.Field(alias="type", default=None)
    us_bank_account: typing.Optional[
        _SerializerPaymentMethodCreateBodyUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
