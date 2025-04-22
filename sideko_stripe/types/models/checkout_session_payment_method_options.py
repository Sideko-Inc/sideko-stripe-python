import pydantic
import typing

from .checkout_acss_debit_payment_method_options import (
    CheckoutAcssDebitPaymentMethodOptions,
)
from .checkout_affirm_payment_method_options import CheckoutAffirmPaymentMethodOptions
from .checkout_afterpay_clearpay_payment_method_options import (
    CheckoutAfterpayClearpayPaymentMethodOptions,
)
from .checkout_alipay_payment_method_options import CheckoutAlipayPaymentMethodOptions
from .checkout_amazon_pay_payment_method_options import (
    CheckoutAmazonPayPaymentMethodOptions,
)
from .checkout_au_becs_debit_payment_method_options import (
    CheckoutAuBecsDebitPaymentMethodOptions,
)
from .checkout_bacs_debit_payment_method_options import (
    CheckoutBacsDebitPaymentMethodOptions,
)
from .checkout_bancontact_payment_method_options import (
    CheckoutBancontactPaymentMethodOptions,
)
from .checkout_boleto_payment_method_options import CheckoutBoletoPaymentMethodOptions
from .checkout_card_payment_method_options import CheckoutCardPaymentMethodOptions
from .checkout_cashapp_payment_method_options import CheckoutCashappPaymentMethodOptions
from .checkout_customer_balance_payment_method_options import (
    CheckoutCustomerBalancePaymentMethodOptions,
)
from .checkout_eps_payment_method_options import CheckoutEpsPaymentMethodOptions
from .checkout_fpx_payment_method_options import CheckoutFpxPaymentMethodOptions
from .checkout_giropay_payment_method_options import CheckoutGiropayPaymentMethodOptions
from .checkout_grab_pay_payment_method_options import (
    CheckoutGrabPayPaymentMethodOptions,
)
from .checkout_ideal_payment_method_options import CheckoutIdealPaymentMethodOptions
from .checkout_kakao_pay_payment_method_options import (
    CheckoutKakaoPayPaymentMethodOptions,
)
from .checkout_klarna_payment_method_options import CheckoutKlarnaPaymentMethodOptions
from .checkout_konbini_payment_method_options import CheckoutKonbiniPaymentMethodOptions
from .checkout_kr_card_payment_method_options import CheckoutKrCardPaymentMethodOptions
from .checkout_link_payment_method_options import CheckoutLinkPaymentMethodOptions
from .checkout_mobilepay_payment_method_options import (
    CheckoutMobilepayPaymentMethodOptions,
)
from .checkout_multibanco_payment_method_options import (
    CheckoutMultibancoPaymentMethodOptions,
)
from .checkout_naver_pay_payment_method_options import (
    CheckoutNaverPayPaymentMethodOptions,
)
from .checkout_oxxo_payment_method_options import CheckoutOxxoPaymentMethodOptions
from .checkout_p24_payment_method_options import CheckoutP24PaymentMethodOptions
from .checkout_payco_payment_method_options import CheckoutPaycoPaymentMethodOptions
from .checkout_paynow_payment_method_options import CheckoutPaynowPaymentMethodOptions
from .checkout_paypal_payment_method_options import CheckoutPaypalPaymentMethodOptions
from .checkout_pix_payment_method_options import CheckoutPixPaymentMethodOptions
from .checkout_revolut_pay_payment_method_options import (
    CheckoutRevolutPayPaymentMethodOptions,
)
from .checkout_samsung_pay_payment_method_options import (
    CheckoutSamsungPayPaymentMethodOptions,
)
from .checkout_sepa_debit_payment_method_options import (
    CheckoutSepaDebitPaymentMethodOptions,
)
from .checkout_sofort_payment_method_options import CheckoutSofortPaymentMethodOptions
from .checkout_swish_payment_method_options import CheckoutSwishPaymentMethodOptions
from .checkout_us_bank_account_payment_method_options import (
    CheckoutUsBankAccountPaymentMethodOptions,
)


class CheckoutSessionPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[CheckoutAcssDebitPaymentMethodOptions] = pydantic.Field(
        alias="acss_debit", default=None
    )
    affirm: typing.Optional[CheckoutAffirmPaymentMethodOptions] = pydantic.Field(
        alias="affirm", default=None
    )
    afterpay_clearpay: typing.Optional[CheckoutAfterpayClearpayPaymentMethodOptions] = (
        pydantic.Field(alias="afterpay_clearpay", default=None)
    )
    alipay: typing.Optional[CheckoutAlipayPaymentMethodOptions] = pydantic.Field(
        alias="alipay", default=None
    )
    amazon_pay: typing.Optional[CheckoutAmazonPayPaymentMethodOptions] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[CheckoutAuBecsDebitPaymentMethodOptions] = (
        pydantic.Field(alias="au_becs_debit", default=None)
    )
    bacs_debit: typing.Optional[CheckoutBacsDebitPaymentMethodOptions] = pydantic.Field(
        alias="bacs_debit", default=None
    )
    bancontact: typing.Optional[CheckoutBancontactPaymentMethodOptions] = (
        pydantic.Field(alias="bancontact", default=None)
    )
    boleto: typing.Optional[CheckoutBoletoPaymentMethodOptions] = pydantic.Field(
        alias="boleto", default=None
    )
    card: typing.Optional[CheckoutCardPaymentMethodOptions] = pydantic.Field(
        alias="card", default=None
    )
    cashapp: typing.Optional[CheckoutCashappPaymentMethodOptions] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer_balance: typing.Optional[CheckoutCustomerBalancePaymentMethodOptions] = (
        pydantic.Field(alias="customer_balance", default=None)
    )
    eps: typing.Optional[CheckoutEpsPaymentMethodOptions] = pydantic.Field(
        alias="eps", default=None
    )
    fpx: typing.Optional[CheckoutFpxPaymentMethodOptions] = pydantic.Field(
        alias="fpx", default=None
    )
    giropay: typing.Optional[CheckoutGiropayPaymentMethodOptions] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[CheckoutGrabPayPaymentMethodOptions] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional[CheckoutIdealPaymentMethodOptions] = pydantic.Field(
        alias="ideal", default=None
    )
    kakao_pay: typing.Optional[CheckoutKakaoPayPaymentMethodOptions] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[CheckoutKlarnaPaymentMethodOptions] = pydantic.Field(
        alias="klarna", default=None
    )
    konbini: typing.Optional[CheckoutKonbiniPaymentMethodOptions] = pydantic.Field(
        alias="konbini", default=None
    )
    kr_card: typing.Optional[CheckoutKrCardPaymentMethodOptions] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[CheckoutLinkPaymentMethodOptions] = pydantic.Field(
        alias="link", default=None
    )
    mobilepay: typing.Optional[CheckoutMobilepayPaymentMethodOptions] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[CheckoutMultibancoPaymentMethodOptions] = (
        pydantic.Field(alias="multibanco", default=None)
    )
    naver_pay: typing.Optional[CheckoutNaverPayPaymentMethodOptions] = pydantic.Field(
        alias="naver_pay", default=None
    )
    oxxo: typing.Optional[CheckoutOxxoPaymentMethodOptions] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[CheckoutP24PaymentMethodOptions] = pydantic.Field(
        alias="p24", default=None
    )
    payco: typing.Optional[CheckoutPaycoPaymentMethodOptions] = pydantic.Field(
        alias="payco", default=None
    )
    paynow: typing.Optional[CheckoutPaynowPaymentMethodOptions] = pydantic.Field(
        alias="paynow", default=None
    )
    paypal: typing.Optional[CheckoutPaypalPaymentMethodOptions] = pydantic.Field(
        alias="paypal", default=None
    )
    pix: typing.Optional[CheckoutPixPaymentMethodOptions] = pydantic.Field(
        alias="pix", default=None
    )
    revolut_pay: typing.Optional[CheckoutRevolutPayPaymentMethodOptions] = (
        pydantic.Field(alias="revolut_pay", default=None)
    )
    samsung_pay: typing.Optional[CheckoutSamsungPayPaymentMethodOptions] = (
        pydantic.Field(alias="samsung_pay", default=None)
    )
    sepa_debit: typing.Optional[CheckoutSepaDebitPaymentMethodOptions] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    sofort: typing.Optional[CheckoutSofortPaymentMethodOptions] = pydantic.Field(
        alias="sofort", default=None
    )
    swish: typing.Optional[CheckoutSwishPaymentMethodOptions] = pydantic.Field(
        alias="swish", default=None
    )
    us_bank_account: typing.Optional[CheckoutUsBankAccountPaymentMethodOptions] = (
        pydantic.Field(alias="us_bank_account", default=None)
    )
