import pydantic
import typing
import typing_extensions

from .billing_details import BillingDetails
from .payment_method_acss_debit import PaymentMethodAcssDebit
from .payment_method_au_becs_debit import PaymentMethodAuBecsDebit
from .payment_method_bacs_debit import PaymentMethodBacsDebit
from .payment_method_boleto import PaymentMethodBoleto
from .payment_method_card_present import PaymentMethodCardPresent
from .payment_method_cashapp import PaymentMethodCashapp
from .payment_method_eps import PaymentMethodEps
from .payment_method_fpx import PaymentMethodFpx
from .payment_method_ideal import PaymentMethodIdeal
from .payment_method_interac_present import PaymentMethodInteracPresent
from .payment_method_klarna import PaymentMethodKlarna
from .payment_method_kr_card import PaymentMethodKrCard
from .payment_method_link import PaymentMethodLink
from .payment_method_naver_pay import PaymentMethodNaverPay
from .payment_method_nz_bank_account import PaymentMethodNzBankAccount
from .payment_method_p24 import PaymentMethodP24
from .payment_method_paypal import PaymentMethodPaypal
from .payment_method_sofort import PaymentMethodSofort
from .payment_method_us_bank_account import PaymentMethodUsBankAccount

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer
    from .payment_method_card import PaymentMethodCard
    from .payment_method_sepa_debit import PaymentMethodSepaDebit


class ConfirmationTokensResourcePaymentMethodPreview(pydantic.BaseModel):
    """
    Details of the PaymentMethod collected by Payment Element
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[PaymentMethodAcssDebit] = pydantic.Field(
        alias="acss_debit", default=None
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
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
    """
    alma: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alma", default=None
    )
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[PaymentMethodAuBecsDebit] = pydantic.Field(
        alias="au_becs_debit", default=None
    )
    bacs_debit: typing.Optional[PaymentMethodBacsDebit] = pydantic.Field(
        alias="bacs_debit", default=None
    )
    bancontact: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="bancontact", default=None
    )
    billie: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="billie", default=None
    )
    billing_details: BillingDetails = pydantic.Field(
        alias="billing_details",
    )
    blik: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="blik", default=None
    )
    boleto: typing.Optional[PaymentMethodBoleto] = pydantic.Field(
        alias="boleto", default=None
    )
    card: typing.Optional["PaymentMethodCard"] = pydantic.Field(
        alias="card", default=None
    )
    card_present: typing.Optional[PaymentMethodCardPresent] = pydantic.Field(
        alias="card_present", default=None
    )
    cashapp: typing.Optional[PaymentMethodCashapp] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer: typing.Optional[typing.Union[str, "Customer"]] = pydantic.Field(
        alias="customer", default=None
    )
    """
    The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
    """
    customer_balance: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="customer_balance", default=None
    )
    eps: typing.Optional[PaymentMethodEps] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[PaymentMethodFpx] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional[PaymentMethodIdeal] = pydantic.Field(
        alias="ideal", default=None
    )
    interac_present: typing.Optional[PaymentMethodInteracPresent] = pydantic.Field(
        alias="interac_present", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[PaymentMethodKlarna] = pydantic.Field(
        alias="klarna", default=None
    )
    konbini: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="konbini", default=None
    )
    kr_card: typing.Optional[PaymentMethodKrCard] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[PaymentMethodLink] = pydantic.Field(
        alias="link", default=None
    )
    mobilepay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="multibanco", default=None
    )
    naver_pay: typing.Optional[PaymentMethodNaverPay] = pydantic.Field(
        alias="naver_pay", default=None
    )
    nz_bank_account: typing.Optional[PaymentMethodNzBankAccount] = pydantic.Field(
        alias="nz_bank_account", default=None
    )
    oxxo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[PaymentMethodP24] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    payco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="payco", default=None
    )
    paynow: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paynow", default=None
    )
    paypal: typing.Optional[PaymentMethodPaypal] = pydantic.Field(
        alias="paypal", default=None
    )
    pix: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pix", default=None
    )
    promptpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="promptpay", default=None
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
    sepa_debit: typing.Optional["PaymentMethodSepaDebit"] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    sofort: typing.Optional[PaymentMethodSofort] = pydantic.Field(
        alias="sofort", default=None
    )
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
        "card",
        "card_present",
        "cashapp",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "grabpay",
        "ideal",
        "interac_present",
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
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: typing.Optional[PaymentMethodUsBankAccount] = pydantic.Field(
        alias="us_bank_account", default=None
    )
    wechat_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
