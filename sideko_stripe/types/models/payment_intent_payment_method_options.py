import pydantic
import typing

from .payment_flows_private_payment_methods_kakao_pay_payment_method_options import (
    PaymentFlowsPrivatePaymentMethodsKakaoPayPaymentMethodOptions,
)
from .payment_flows_private_payment_methods_naver_pay_payment_method_options import (
    PaymentFlowsPrivatePaymentMethodsNaverPayPaymentMethodOptions,
)
from .payment_flows_private_payment_methods_payco_payment_method_options import (
    PaymentFlowsPrivatePaymentMethodsPaycoPaymentMethodOptions,
)
from .payment_flows_private_payment_methods_samsung_pay_payment_method_options import (
    PaymentFlowsPrivatePaymentMethodsSamsungPayPaymentMethodOptions,
)
from .payment_intent_payment_method_options_acss_debit1 import (
    PaymentIntentPaymentMethodOptionsAcssDebit1,
)
from .payment_intent_payment_method_options_au_becs_debit1 import (
    PaymentIntentPaymentMethodOptionsAuBecsDebit1,
)
from .payment_intent_payment_method_options_bacs_debit1 import (
    PaymentIntentPaymentMethodOptionsBacsDebit1,
)
from .payment_intent_payment_method_options_blik1 import (
    PaymentIntentPaymentMethodOptionsBlik1,
)
from .payment_intent_payment_method_options_card1 import (
    PaymentIntentPaymentMethodOptionsCard1,
)
from .payment_intent_payment_method_options_eps1 import (
    PaymentIntentPaymentMethodOptionsEps1,
)
from .payment_intent_payment_method_options_link1 import (
    PaymentIntentPaymentMethodOptionsLink1,
)
from .payment_intent_payment_method_options_mobilepay1 import (
    PaymentIntentPaymentMethodOptionsMobilepay1,
)
from .payment_intent_payment_method_options_nz_bank_account1 import (
    PaymentIntentPaymentMethodOptionsNzBankAccount1,
)
from .payment_intent_payment_method_options_sepa_debit1 import (
    PaymentIntentPaymentMethodOptionsSepaDebit1,
)
from .payment_intent_payment_method_options_swish1 import (
    PaymentIntentPaymentMethodOptionsSwish1,
)
from .payment_intent_payment_method_options_us_bank_account1 import (
    PaymentIntentPaymentMethodOptionsUsBankAccount1,
)
from .payment_intent_type_specific_payment_method_options_client import (
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
)
from .payment_method_options_affirm import PaymentMethodOptionsAffirm
from .payment_method_options_afterpay_clearpay import (
    PaymentMethodOptionsAfterpayClearpay,
)
from .payment_method_options_alipay import PaymentMethodOptionsAlipay
from .payment_method_options_alma import PaymentMethodOptionsAlma
from .payment_method_options_amazon_pay import PaymentMethodOptionsAmazonPay
from .payment_method_options_bancontact import PaymentMethodOptionsBancontact
from .payment_method_options_boleto import PaymentMethodOptionsBoleto
from .payment_method_options_card_present import PaymentMethodOptionsCardPresent
from .payment_method_options_cashapp import PaymentMethodOptionsCashapp
from .payment_method_options_customer_balance import PaymentMethodOptionsCustomerBalance
from .payment_method_options_fpx import PaymentMethodOptionsFpx
from .payment_method_options_giropay import PaymentMethodOptionsGiropay
from .payment_method_options_grabpay import PaymentMethodOptionsGrabpay
from .payment_method_options_ideal import PaymentMethodOptionsIdeal
from .payment_method_options_klarna import PaymentMethodOptionsKlarna
from .payment_method_options_konbini import PaymentMethodOptionsKonbini
from .payment_method_options_kr_card import PaymentMethodOptionsKrCard
from .payment_method_options_multibanco import PaymentMethodOptionsMultibanco
from .payment_method_options_oxxo import PaymentMethodOptionsOxxo
from .payment_method_options_p24 import PaymentMethodOptionsP24
from .payment_method_options_paynow import PaymentMethodOptionsPaynow
from .payment_method_options_paypal import PaymentMethodOptionsPaypal
from .payment_method_options_pix import PaymentMethodOptionsPix
from .payment_method_options_promptpay import PaymentMethodOptionsPromptpay
from .payment_method_options_revolut_pay import PaymentMethodOptionsRevolutPay
from .payment_method_options_sofort import PaymentMethodOptionsSofort
from .payment_method_options_twint import PaymentMethodOptionsTwint
from .payment_method_options_wechat_pay import PaymentMethodOptionsWechatPay
from .payment_method_options_zip import PaymentMethodOptionsZip


class PaymentIntentPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsAcssDebit1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[
        typing.Union[
            PaymentMethodOptionsAffirm,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="affirm", default=None)
    afterpay_clearpay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsAfterpayClearpay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsAlipay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="alipay", default=None)
    alma: typing.Optional[
        typing.Union[
            PaymentMethodOptionsAlma,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="alma", default=None)
    amazon_pay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsAmazonPay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="amazon_pay", default=None)
    au_becs_debit: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsAuBecsDebit1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsBacsDebit1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            PaymentMethodOptionsBancontact,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    blik: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsBlik1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="blik", default=None)
    boleto: typing.Optional[
        typing.Union[
            PaymentMethodOptionsBoleto,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="boleto", default=None)
    card: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsCard1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[
        typing.Union[
            PaymentMethodOptionsCardPresent,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="card_present", default=None)
    cashapp: typing.Optional[
        typing.Union[
            PaymentMethodOptionsCashapp,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="cashapp", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            PaymentMethodOptionsCustomerBalance,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsEps1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[
        typing.Union[
            PaymentMethodOptionsFpx, PaymentIntentTypeSpecificPaymentMethodOptionsClient
        ]
    ] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsGiropay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="giropay", default=None)
    grabpay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsGrabpay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="grabpay", default=None)
    ideal: typing.Optional[
        typing.Union[
            PaymentMethodOptionsIdeal,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="ideal", default=None)
    interac_present: typing.Optional[
        typing.Union[
            typing.Dict[str, typing.Any],
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="interac_present", default=None)
    kakao_pay: typing.Optional[
        typing.Union[
            PaymentFlowsPrivatePaymentMethodsKakaoPayPaymentMethodOptions,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="kakao_pay", default=None)
    klarna: typing.Optional[
        typing.Union[
            PaymentMethodOptionsKlarna,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[
        typing.Union[
            PaymentMethodOptionsKonbini,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="konbini", default=None)
    kr_card: typing.Optional[
        typing.Union[
            PaymentMethodOptionsKrCard,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="kr_card", default=None)
    link: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsLink1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="link", default=None)
    mobilepay: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsMobilepay1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        typing.Union[
            PaymentMethodOptionsMultibanco,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="multibanco", default=None)
    naver_pay: typing.Optional[
        typing.Union[
            PaymentFlowsPrivatePaymentMethodsNaverPayPaymentMethodOptions,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsNzBankAccount1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[
        typing.Union[
            PaymentMethodOptionsOxxo,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="oxxo", default=None)
    p24: typing.Optional[
        typing.Union[
            PaymentMethodOptionsP24, PaymentIntentTypeSpecificPaymentMethodOptionsClient
        ]
    ] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[
        typing.Union[
            typing.Dict[str, typing.Any],
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="pay_by_bank", default=None)
    payco: typing.Optional[
        typing.Union[
            PaymentFlowsPrivatePaymentMethodsPaycoPaymentMethodOptions,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="payco", default=None)
    paynow: typing.Optional[
        typing.Union[
            PaymentMethodOptionsPaynow,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="paynow", default=None)
    paypal: typing.Optional[
        typing.Union[
            PaymentMethodOptionsPaypal,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="paypal", default=None)
    pix: typing.Optional[
        typing.Union[
            PaymentMethodOptionsPix, PaymentIntentTypeSpecificPaymentMethodOptionsClient
        ]
    ] = pydantic.Field(alias="pix", default=None)
    promptpay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsPromptpay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="promptpay", default=None)
    revolut_pay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsRevolutPay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="revolut_pay", default=None)
    samsung_pay: typing.Optional[
        typing.Union[
            PaymentFlowsPrivatePaymentMethodsSamsungPayPaymentMethodOptions,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="samsung_pay", default=None)
    sepa_debit: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsSepaDebit1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        typing.Union[
            PaymentMethodOptionsSofort,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsSwish1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="swish", default=None)
    twint: typing.Optional[
        typing.Union[
            PaymentMethodOptionsTwint,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="twint", default=None)
    us_bank_account: typing.Optional[
        typing.Union[
            PaymentIntentPaymentMethodOptionsUsBankAccount1,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        typing.Union[
            PaymentMethodOptionsWechatPay,
            PaymentIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="wechat_pay", default=None)
    zip: typing.Optional[
        typing.Union[
            PaymentMethodOptionsZip, PaymentIntentTypeSpecificPaymentMethodOptionsClient
        ]
    ] = pydantic.Field(alias="zip", default=None)
