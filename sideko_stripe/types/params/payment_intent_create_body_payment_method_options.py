import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_acss_debit_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAcssDebitObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAcssDebitObj0,
)
from .payment_intent_create_body_payment_method_options_affirm_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAffirmObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAffirmObj0,
)
from .payment_intent_create_body_payment_method_options_afterpay_clearpay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAfterpayClearpayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAfterpayClearpayObj0,
)
from .payment_intent_create_body_payment_method_options_alipay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAlipayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAlipayObj0,
)
from .payment_intent_create_body_payment_method_options_alma_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0,
)
from .payment_intent_create_body_payment_method_options_amazon_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAmazonPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAmazonPayObj0,
)
from .payment_intent_create_body_payment_method_options_au_becs_debit_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsAuBecsDebitObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAuBecsDebitObj0,
)
from .payment_intent_create_body_payment_method_options_bacs_debit_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0,
)
from .payment_intent_create_body_payment_method_options_bancontact_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsBancontactObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBancontactObj0,
)
from .payment_intent_create_body_payment_method_options_blik_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsBlikObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBlikObj0,
)
from .payment_intent_create_body_payment_method_options_boleto_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0,
)
from .payment_intent_create_body_payment_method_options_card_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0,
)
from .payment_intent_create_body_payment_method_options_card_present_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0,
)
from .payment_intent_create_body_payment_method_options_cashapp_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsCashappObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCashappObj0,
)
from .payment_intent_create_body_payment_method_options_customer_balance_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0,
)
from .payment_intent_create_body_payment_method_options_eps_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsEpsObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsEpsObj0,
)
from .payment_intent_create_body_payment_method_options_fpx_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsFpxObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsFpxObj0,
)
from .payment_intent_create_body_payment_method_options_giropay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsGiropayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsGiropayObj0,
)
from .payment_intent_create_body_payment_method_options_grabpay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsGrabpayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsGrabpayObj0,
)
from .payment_intent_create_body_payment_method_options_ideal_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsIdealObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsIdealObj0,
)
from .payment_intent_create_body_payment_method_options_kakao_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsKakaoPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKakaoPayObj0,
)
from .payment_intent_create_body_payment_method_options_klarna_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsKlarnaObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKlarnaObj0,
)
from .payment_intent_create_body_payment_method_options_konbini_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0,
)
from .payment_intent_create_body_payment_method_options_kr_card_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsKrCardObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKrCardObj0,
)
from .payment_intent_create_body_payment_method_options_link_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsLinkObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsLinkObj0,
)
from .payment_intent_create_body_payment_method_options_mobilepay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsMobilepayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsMobilepayObj0,
)
from .payment_intent_create_body_payment_method_options_multibanco_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsMultibancoObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsMultibancoObj0,
)
from .payment_intent_create_body_payment_method_options_naver_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsNaverPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsNaverPayObj0,
)
from .payment_intent_create_body_payment_method_options_nz_bank_account_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0,
)
from .payment_intent_create_body_payment_method_options_oxxo_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0,
)
from .payment_intent_create_body_payment_method_options_p24_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsP24Obj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsP24Obj0,
)
from .payment_intent_create_body_payment_method_options_payco_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0,
)
from .payment_intent_create_body_payment_method_options_paynow_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsPaynowObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaynowObj0,
)
from .payment_intent_create_body_payment_method_options_paypal_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsPaypalObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaypalObj0,
)
from .payment_intent_create_body_payment_method_options_pix_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsPixObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPixObj0,
)
from .payment_intent_create_body_payment_method_options_promptpay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsPromptpayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPromptpayObj0,
)
from .payment_intent_create_body_payment_method_options_revolut_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsRevolutPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsRevolutPayObj0,
)
from .payment_intent_create_body_payment_method_options_samsung_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsSamsungPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSamsungPayObj0,
)
from .payment_intent_create_body_payment_method_options_sepa_debit_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0,
)
from .payment_intent_create_body_payment_method_options_sofort_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsSofortObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSofortObj0,
)
from .payment_intent_create_body_payment_method_options_swish_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsSwishObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSwishObj0,
)
from .payment_intent_create_body_payment_method_options_twint_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsTwintObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsTwintObj0,
)
from .payment_intent_create_body_payment_method_options_us_bank_account_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0,
)
from .payment_intent_create_body_payment_method_options_wechat_pay_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0,
)
from .payment_intent_create_body_payment_method_options_zip_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsZipObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsZipObj0,
)


class PaymentIntentCreateBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment method-specific configuration for this PaymentIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAcssDebitObj0, str]
    ]

    affirm: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAffirmObj0, str]
    ]

    afterpay_clearpay: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentCreateBodyPaymentMethodOptionsAfterpayClearpayObj0, str
        ]
    ]

    alipay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAlipayObj0, str]
    ]

    alma: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0, str]
    ]

    amazon_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAmazonPayObj0, str]
    ]

    au_becs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsAuBecsDebitObj0, str]
    ]

    bacs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0, str]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsBancontactObj0, str]
    ]

    blik: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsBlikObj0, str]
    ]

    boleto: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0, str]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsCardObj0, str]
    ]

    card_present: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0, str]
    ]

    cashapp: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsCashappObj0, str]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0, str
        ]
    ]

    eps: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsEpsObj0, str]
    ]

    fpx: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsFpxObj0, str]
    ]

    giropay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsGiropayObj0, str]
    ]

    grabpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsGrabpayObj0, str]
    ]

    ideal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsIdealObj0, str]
    ]

    interac_present: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    kakao_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsKakaoPayObj0, str]
    ]

    klarna: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsKlarnaObj0, str]
    ]

    konbini: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0, str]
    ]

    kr_card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsKrCardObj0, str]
    ]

    link: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsLinkObj0, str]
    ]

    mobilepay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsMobilepayObj0, str]
    ]

    multibanco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsMultibancoObj0, str]
    ]

    naver_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsNaverPayObj0, str]
    ]

    nz_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0, str]
    ]

    oxxo: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0, str]
    ]

    p24: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsP24Obj0, str]
    ]

    pay_by_bank: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    payco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0, str]
    ]

    paynow: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsPaynowObj0, str]
    ]

    paypal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsPaypalObj0, str]
    ]

    pix: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsPixObj0, str]
    ]

    promptpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsPromptpayObj0, str]
    ]

    revolut_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsRevolutPayObj0, str]
    ]

    samsung_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsSamsungPayObj0, str]
    ]

    sepa_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0, str]
    ]

    sofort: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsSofortObj0, str]
    ]

    swish: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsSwishObj0, str]
    ]

    twint: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsTwintObj0, str]
    ]

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0, str]
    ]

    wechat_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0, str]
    ]

    zip: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyPaymentMethodOptionsZipObj0, str]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAcssDebitObj0, str
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAffirmObj0, str
        ]
    ] = pydantic.Field(alias="affirm", default=None)
    afterpay_clearpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAfterpayClearpayObj0,
            str,
        ]
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAlipayObj0, str
        ]
    ] = pydantic.Field(alias="alipay", default=None)
    alma: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0, str
        ]
    ] = pydantic.Field(alias="alma", default=None)
    amazon_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAmazonPayObj0, str
        ]
    ] = pydantic.Field(alias="amazon_pay", default=None)
    au_becs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAuBecsDebitObj0, str
        ]
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0, str
        ]
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBancontactObj0, str
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    blik: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBlikObj0, str
        ]
    ] = pydantic.Field(alias="blik", default=None)
    boleto: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBoletoObj0, str
        ]
    ] = pydantic.Field(alias="boleto", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0, str
        ]
    ] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0, str
        ]
    ] = pydantic.Field(alias="card_present", default=None)
    cashapp: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCashappObj0, str
        ]
    ] = pydantic.Field(alias="cashapp", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0,
            str,
        ]
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyPaymentMethodOptionsEpsObj0, str]
    ] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyPaymentMethodOptionsFpxObj0, str]
    ] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsGiropayObj0, str
        ]
    ] = pydantic.Field(alias="giropay", default=None)
    grabpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsGrabpayObj0, str
        ]
    ] = pydantic.Field(alias="grabpay", default=None)
    ideal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsIdealObj0, str
        ]
    ] = pydantic.Field(alias="ideal", default=None)
    interac_present: typing.Optional[
        typing.Union[typing.Dict[str, typing.Any], str]
    ] = pydantic.Field(alias="interac_present", default=None)
    kakao_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKakaoPayObj0, str
        ]
    ] = pydantic.Field(alias="kakao_pay", default=None)
    klarna: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKlarnaObj0, str
        ]
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0, str
        ]
    ] = pydantic.Field(alias="konbini", default=None)
    kr_card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKrCardObj0, str
        ]
    ] = pydantic.Field(alias="kr_card", default=None)
    link: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsLinkObj0, str
        ]
    ] = pydantic.Field(alias="link", default=None)
    mobilepay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsMobilepayObj0, str
        ]
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsMultibancoObj0, str
        ]
    ] = pydantic.Field(alias="multibanco", default=None)
    naver_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsNaverPayObj0, str
        ]
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0, str
        ]
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsOxxoObj0, str
        ]
    ] = pydantic.Field(alias="oxxo", default=None)
    p24: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyPaymentMethodOptionsP24Obj0, str]
    ] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = (
        pydantic.Field(alias="pay_by_bank", default=None)
    )
    payco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaycoObj0, str
        ]
    ] = pydantic.Field(alias="payco", default=None)
    paynow: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaynowObj0, str
        ]
    ] = pydantic.Field(alias="paynow", default=None)
    paypal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPaypalObj0, str
        ]
    ] = pydantic.Field(alias="paypal", default=None)
    pix: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyPaymentMethodOptionsPixObj0, str]
    ] = pydantic.Field(alias="pix", default=None)
    promptpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsPromptpayObj0, str
        ]
    ] = pydantic.Field(alias="promptpay", default=None)
    revolut_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsRevolutPayObj0, str
        ]
    ] = pydantic.Field(alias="revolut_pay", default=None)
    samsung_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSamsungPayObj0, str
        ]
    ] = pydantic.Field(alias="samsung_pay", default=None)
    sepa_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0, str
        ]
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSofortObj0, str
        ]
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSwishObj0, str
        ]
    ] = pydantic.Field(alias="swish", default=None)
    twint: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsTwintObj0, str
        ]
    ] = pydantic.Field(alias="twint", default=None)
    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0, str
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsWechatPayObj0, str
        ]
    ] = pydantic.Field(alias="wechat_pay", default=None)
    zip: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyPaymentMethodOptionsZipObj0, str]
    ] = pydantic.Field(alias="zip", default=None)
