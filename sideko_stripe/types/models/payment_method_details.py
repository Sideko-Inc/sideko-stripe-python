import pydantic
import typing
import typing_extensions

from .payment_flows_private_payment_methods_alipay_details import (
    PaymentFlowsPrivatePaymentMethodsAlipayDetails,
)
from .payment_method_details_ach_credit_transfer import (
    PaymentMethodDetailsAchCreditTransfer,
)
from .payment_method_details_ach_debit import PaymentMethodDetailsAchDebit
from .payment_method_details_acss_debit import PaymentMethodDetailsAcssDebit
from .payment_method_details_affirm import PaymentMethodDetailsAffirm
from .payment_method_details_afterpay_clearpay import (
    PaymentMethodDetailsAfterpayClearpay,
)
from .payment_method_details_amazon_pay import PaymentMethodDetailsAmazonPay
from .payment_method_details_au_becs_debit import PaymentMethodDetailsAuBecsDebit
from .payment_method_details_bacs_debit import PaymentMethodDetailsBacsDebit
from .payment_method_details_blik import PaymentMethodDetailsBlik
from .payment_method_details_boleto import PaymentMethodDetailsBoleto
from .payment_method_details_card import PaymentMethodDetailsCard
from .payment_method_details_card_present import PaymentMethodDetailsCardPresent
from .payment_method_details_cashapp import PaymentMethodDetailsCashapp
from .payment_method_details_eps import PaymentMethodDetailsEps
from .payment_method_details_fpx import PaymentMethodDetailsFpx
from .payment_method_details_giropay import PaymentMethodDetailsGiropay
from .payment_method_details_grabpay import PaymentMethodDetailsGrabpay
from .payment_method_details_interac_present import PaymentMethodDetailsInteracPresent
from .payment_method_details_kakao_pay import PaymentMethodDetailsKakaoPay
from .payment_method_details_klarna import PaymentMethodDetailsKlarna
from .payment_method_details_konbini import PaymentMethodDetailsKonbini
from .payment_method_details_kr_card import PaymentMethodDetailsKrCard
from .payment_method_details_link import PaymentMethodDetailsLink
from .payment_method_details_mobilepay import PaymentMethodDetailsMobilepay
from .payment_method_details_multibanco import PaymentMethodDetailsMultibanco
from .payment_method_details_naver_pay import PaymentMethodDetailsNaverPay
from .payment_method_details_nz_bank_account import PaymentMethodDetailsNzBankAccount
from .payment_method_details_oxxo import PaymentMethodDetailsOxxo
from .payment_method_details_p24 import PaymentMethodDetailsP24
from .payment_method_details_payco import PaymentMethodDetailsPayco
from .payment_method_details_paynow import PaymentMethodDetailsPaynow
from .payment_method_details_paypal import PaymentMethodDetailsPaypal
from .payment_method_details_pix import PaymentMethodDetailsPix
from .payment_method_details_promptpay import PaymentMethodDetailsPromptpay
from .payment_method_details_revolut_pay import PaymentMethodDetailsRevolutPay
from .payment_method_details_samsung_pay import PaymentMethodDetailsSamsungPay
from .payment_method_details_sepa_debit import PaymentMethodDetailsSepaDebit
from .payment_method_details_swish import PaymentMethodDetailsSwish
from .payment_method_details_wechat_pay import PaymentMethodDetailsWechatPay

if typing_extensions.TYPE_CHECKING:
    from .payment_method_details_bancontact import PaymentMethodDetailsBancontact
    from .payment_method_details_ideal import PaymentMethodDetailsIdeal
    from .payment_method_details_sofort import PaymentMethodDetailsSofort
    from .payment_method_details_us_bank_account import (
        PaymentMethodDetailsUsBankAccount,
    )


class PaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach_credit_transfer: typing.Optional[PaymentMethodDetailsAchCreditTransfer] = (
        pydantic.Field(alias="ach_credit_transfer", default=None)
    )
    ach_debit: typing.Optional[PaymentMethodDetailsAchDebit] = pydantic.Field(
        alias="ach_debit", default=None
    )
    acss_debit: typing.Optional[PaymentMethodDetailsAcssDebit] = pydantic.Field(
        alias="acss_debit", default=None
    )
    affirm: typing.Optional[PaymentMethodDetailsAffirm] = pydantic.Field(
        alias="affirm", default=None
    )
    afterpay_clearpay: typing.Optional[PaymentMethodDetailsAfterpayClearpay] = (
        pydantic.Field(alias="afterpay_clearpay", default=None)
    )
    alipay: typing.Optional[PaymentFlowsPrivatePaymentMethodsAlipayDetails] = (
        pydantic.Field(alias="alipay", default=None)
    )
    alma: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alma", default=None
    )
    amazon_pay: typing.Optional[PaymentMethodDetailsAmazonPay] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[PaymentMethodDetailsAuBecsDebit] = pydantic.Field(
        alias="au_becs_debit", default=None
    )
    bacs_debit: typing.Optional[PaymentMethodDetailsBacsDebit] = pydantic.Field(
        alias="bacs_debit", default=None
    )
    bancontact: typing.Optional["PaymentMethodDetailsBancontact"] = pydantic.Field(
        alias="bancontact", default=None
    )
    billie: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="billie", default=None
    )
    blik: typing.Optional[PaymentMethodDetailsBlik] = pydantic.Field(
        alias="blik", default=None
    )
    boleto: typing.Optional[PaymentMethodDetailsBoleto] = pydantic.Field(
        alias="boleto", default=None
    )
    card: typing.Optional[PaymentMethodDetailsCard] = pydantic.Field(
        alias="card", default=None
    )
    card_present: typing.Optional[PaymentMethodDetailsCardPresent] = pydantic.Field(
        alias="card_present", default=None
    )
    cashapp: typing.Optional[PaymentMethodDetailsCashapp] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer_balance: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="customer_balance", default=None
    )
    eps: typing.Optional[PaymentMethodDetailsEps] = pydantic.Field(
        alias="eps", default=None
    )
    fpx: typing.Optional[PaymentMethodDetailsFpx] = pydantic.Field(
        alias="fpx", default=None
    )
    giropay: typing.Optional[PaymentMethodDetailsGiropay] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[PaymentMethodDetailsGrabpay] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional["PaymentMethodDetailsIdeal"] = pydantic.Field(
        alias="ideal", default=None
    )
    interac_present: typing.Optional[PaymentMethodDetailsInteracPresent] = (
        pydantic.Field(alias="interac_present", default=None)
    )
    kakao_pay: typing.Optional[PaymentMethodDetailsKakaoPay] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[PaymentMethodDetailsKlarna] = pydantic.Field(
        alias="klarna", default=None
    )
    konbini: typing.Optional[PaymentMethodDetailsKonbini] = pydantic.Field(
        alias="konbini", default=None
    )
    kr_card: typing.Optional[PaymentMethodDetailsKrCard] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[PaymentMethodDetailsLink] = pydantic.Field(
        alias="link", default=None
    )
    mobilepay: typing.Optional[PaymentMethodDetailsMobilepay] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[PaymentMethodDetailsMultibanco] = pydantic.Field(
        alias="multibanco", default=None
    )
    naver_pay: typing.Optional[PaymentMethodDetailsNaverPay] = pydantic.Field(
        alias="naver_pay", default=None
    )
    nz_bank_account: typing.Optional[PaymentMethodDetailsNzBankAccount] = (
        pydantic.Field(alias="nz_bank_account", default=None)
    )
    oxxo: typing.Optional[PaymentMethodDetailsOxxo] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[PaymentMethodDetailsP24] = pydantic.Field(
        alias="p24", default=None
    )
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    payco: typing.Optional[PaymentMethodDetailsPayco] = pydantic.Field(
        alias="payco", default=None
    )
    paynow: typing.Optional[PaymentMethodDetailsPaynow] = pydantic.Field(
        alias="paynow", default=None
    )
    paypal: typing.Optional[PaymentMethodDetailsPaypal] = pydantic.Field(
        alias="paypal", default=None
    )
    pix: typing.Optional[PaymentMethodDetailsPix] = pydantic.Field(
        alias="pix", default=None
    )
    promptpay: typing.Optional[PaymentMethodDetailsPromptpay] = pydantic.Field(
        alias="promptpay", default=None
    )
    revolut_pay: typing.Optional[PaymentMethodDetailsRevolutPay] = pydantic.Field(
        alias="revolut_pay", default=None
    )
    samsung_pay: typing.Optional[PaymentMethodDetailsSamsungPay] = pydantic.Field(
        alias="samsung_pay", default=None
    )
    satispay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="satispay", default=None
    )
    sepa_debit: typing.Optional[PaymentMethodDetailsSepaDebit] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    sofort: typing.Optional["PaymentMethodDetailsSofort"] = pydantic.Field(
        alias="sofort", default=None
    )
    stripe_account: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="stripe_account", default=None
    )
    swish: typing.Optional[PaymentMethodDetailsSwish] = pydantic.Field(
        alias="swish", default=None
    )
    twint: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="twint", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of transaction-specific details of the payment method used in the payment. See [PaymentMethod.type](https://stripe.com/docs/api/payment_methods/object#payment_method_object-type) for the full list of possible types.
    An additional hash is included on `payment_method_details` with a name matching this value.
    It contains information specific to the payment method.
    """
    us_bank_account: typing.Optional["PaymentMethodDetailsUsBankAccount"] = (
        pydantic.Field(alias="us_bank_account", default=None)
    )
    wechat: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat", default=None
    )
    wechat_pay: typing.Optional[PaymentMethodDetailsWechatPay] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
