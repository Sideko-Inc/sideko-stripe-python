import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_acss_debit_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0,
)
from .payment_intent_update_body_payment_method_options_affirm_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAffirmObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAffirmObj0,
)
from .payment_intent_update_body_payment_method_options_afterpay_clearpay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAfterpayClearpayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAfterpayClearpayObj0,
)
from .payment_intent_update_body_payment_method_options_alipay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAlipayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAlipayObj0,
)
from .payment_intent_update_body_payment_method_options_alma_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAlmaObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAlmaObj0,
)
from .payment_intent_update_body_payment_method_options_amazon_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAmazonPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAmazonPayObj0,
)
from .payment_intent_update_body_payment_method_options_au_becs_debit_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsAuBecsDebitObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAuBecsDebitObj0,
)
from .payment_intent_update_body_payment_method_options_bacs_debit_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0,
)
from .payment_intent_update_body_payment_method_options_bancontact_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsBancontactObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBancontactObj0,
)
from .payment_intent_update_body_payment_method_options_blik_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsBlikObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBlikObj0,
)
from .payment_intent_update_body_payment_method_options_boleto_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsBoletoObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBoletoObj0,
)
from .payment_intent_update_body_payment_method_options_card_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0,
)
from .payment_intent_update_body_payment_method_options_card_present_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0,
)
from .payment_intent_update_body_payment_method_options_cashapp_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCashappObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCashappObj0,
)
from .payment_intent_update_body_payment_method_options_customer_balance_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0,
)
from .payment_intent_update_body_payment_method_options_eps_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsEpsObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsEpsObj0,
)
from .payment_intent_update_body_payment_method_options_fpx_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsFpxObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsFpxObj0,
)
from .payment_intent_update_body_payment_method_options_giropay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsGiropayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsGiropayObj0,
)
from .payment_intent_update_body_payment_method_options_grabpay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsGrabpayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsGrabpayObj0,
)
from .payment_intent_update_body_payment_method_options_ideal_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsIdealObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsIdealObj0,
)
from .payment_intent_update_body_payment_method_options_kakao_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsKakaoPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKakaoPayObj0,
)
from .payment_intent_update_body_payment_method_options_klarna_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsKlarnaObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKlarnaObj0,
)
from .payment_intent_update_body_payment_method_options_konbini_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsKonbiniObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKonbiniObj0,
)
from .payment_intent_update_body_payment_method_options_kr_card_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsKrCardObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKrCardObj0,
)
from .payment_intent_update_body_payment_method_options_link_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsLinkObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsLinkObj0,
)
from .payment_intent_update_body_payment_method_options_mobilepay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsMobilepayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsMobilepayObj0,
)
from .payment_intent_update_body_payment_method_options_multibanco_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsMultibancoObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsMultibancoObj0,
)
from .payment_intent_update_body_payment_method_options_naver_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsNaverPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsNaverPayObj0,
)
from .payment_intent_update_body_payment_method_options_nz_bank_account_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsNzBankAccountObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsNzBankAccountObj0,
)
from .payment_intent_update_body_payment_method_options_oxxo_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsOxxoObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsOxxoObj0,
)
from .payment_intent_update_body_payment_method_options_p24_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0,
)
from .payment_intent_update_body_payment_method_options_payco_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsPaycoObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaycoObj0,
)
from .payment_intent_update_body_payment_method_options_paynow_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsPaynowObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaynowObj0,
)
from .payment_intent_update_body_payment_method_options_paypal_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsPaypalObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaypalObj0,
)
from .payment_intent_update_body_payment_method_options_pix_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsPixObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPixObj0,
)
from .payment_intent_update_body_payment_method_options_promptpay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsPromptpayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPromptpayObj0,
)
from .payment_intent_update_body_payment_method_options_revolut_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsRevolutPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsRevolutPayObj0,
)
from .payment_intent_update_body_payment_method_options_samsung_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsSamsungPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSamsungPayObj0,
)
from .payment_intent_update_body_payment_method_options_sepa_debit_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0,
)
from .payment_intent_update_body_payment_method_options_sofort_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsSofortObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSofortObj0,
)
from .payment_intent_update_body_payment_method_options_swish_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0,
)
from .payment_intent_update_body_payment_method_options_twint_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0,
)
from .payment_intent_update_body_payment_method_options_us_bank_account_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0,
)
from .payment_intent_update_body_payment_method_options_wechat_pay_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsWechatPayObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsWechatPayObj0,
)
from .payment_intent_update_body_payment_method_options_zip_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsZipObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsZipObj0,
)


class PaymentIntentUpdateBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment-method-specific configuration for this PaymentIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0, str]
    ]

    affirm: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAffirmObj0, str]
    ]

    afterpay_clearpay: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentUpdateBodyPaymentMethodOptionsAfterpayClearpayObj0, str
        ]
    ]

    alipay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAlipayObj0, str]
    ]

    alma: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAlmaObj0, str]
    ]

    amazon_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAmazonPayObj0, str]
    ]

    au_becs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsAuBecsDebitObj0, str]
    ]

    bacs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0, str]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsBancontactObj0, str]
    ]

    blik: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsBlikObj0, str]
    ]

    boleto: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsBoletoObj0, str]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0, str]
    ]

    card_present: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0, str]
    ]

    cashapp: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsCashappObj0, str]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0, str
        ]
    ]

    eps: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsEpsObj0, str]
    ]

    fpx: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsFpxObj0, str]
    ]

    giropay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsGiropayObj0, str]
    ]

    grabpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsGrabpayObj0, str]
    ]

    ideal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsIdealObj0, str]
    ]

    interac_present: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    kakao_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsKakaoPayObj0, str]
    ]

    klarna: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsKlarnaObj0, str]
    ]

    konbini: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsKonbiniObj0, str]
    ]

    kr_card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsKrCardObj0, str]
    ]

    link: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsLinkObj0, str]
    ]

    mobilepay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsMobilepayObj0, str]
    ]

    multibanco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsMultibancoObj0, str]
    ]

    naver_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsNaverPayObj0, str]
    ]

    nz_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsNzBankAccountObj0, str]
    ]

    oxxo: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsOxxoObj0, str]
    ]

    p24: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0, str]
    ]

    pay_by_bank: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    payco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsPaycoObj0, str]
    ]

    paynow: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsPaynowObj0, str]
    ]

    paypal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsPaypalObj0, str]
    ]

    pix: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsPixObj0, str]
    ]

    promptpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsPromptpayObj0, str]
    ]

    revolut_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsRevolutPayObj0, str]
    ]

    samsung_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsSamsungPayObj0, str]
    ]

    sepa_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0, str]
    ]

    sofort: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsSofortObj0, str]
    ]

    swish: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0, str]
    ]

    twint: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0, str]
    ]

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0, str]
    ]

    wechat_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsWechatPayObj0, str]
    ]

    zip: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyPaymentMethodOptionsZipObj0, str]
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0, str
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAffirmObj0, str
        ]
    ] = pydantic.Field(alias="affirm", default=None)
    afterpay_clearpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAfterpayClearpayObj0,
            str,
        ]
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAlipayObj0, str
        ]
    ] = pydantic.Field(alias="alipay", default=None)
    alma: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAlmaObj0, str
        ]
    ] = pydantic.Field(alias="alma", default=None)
    amazon_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAmazonPayObj0, str
        ]
    ] = pydantic.Field(alias="amazon_pay", default=None)
    au_becs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAuBecsDebitObj0, str
        ]
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0, str
        ]
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBancontactObj0, str
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    blik: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBlikObj0, str
        ]
    ] = pydantic.Field(alias="blik", default=None)
    boleto: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBoletoObj0, str
        ]
    ] = pydantic.Field(alias="boleto", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0, str
        ]
    ] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0, str
        ]
    ] = pydantic.Field(alias="card_present", default=None)
    cashapp: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCashappObj0, str
        ]
    ] = pydantic.Field(alias="cashapp", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0,
            str,
        ]
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyPaymentMethodOptionsEpsObj0, str]
    ] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyPaymentMethodOptionsFpxObj0, str]
    ] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsGiropayObj0, str
        ]
    ] = pydantic.Field(alias="giropay", default=None)
    grabpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsGrabpayObj0, str
        ]
    ] = pydantic.Field(alias="grabpay", default=None)
    ideal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsIdealObj0, str
        ]
    ] = pydantic.Field(alias="ideal", default=None)
    interac_present: typing.Optional[
        typing.Union[typing.Dict[str, typing.Any], str]
    ] = pydantic.Field(alias="interac_present", default=None)
    kakao_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKakaoPayObj0, str
        ]
    ] = pydantic.Field(alias="kakao_pay", default=None)
    klarna: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKlarnaObj0, str
        ]
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKonbiniObj0, str
        ]
    ] = pydantic.Field(alias="konbini", default=None)
    kr_card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsKrCardObj0, str
        ]
    ] = pydantic.Field(alias="kr_card", default=None)
    link: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsLinkObj0, str
        ]
    ] = pydantic.Field(alias="link", default=None)
    mobilepay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsMobilepayObj0, str
        ]
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsMultibancoObj0, str
        ]
    ] = pydantic.Field(alias="multibanco", default=None)
    naver_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsNaverPayObj0, str
        ]
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsNzBankAccountObj0, str
        ]
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsOxxoObj0, str
        ]
    ] = pydantic.Field(alias="oxxo", default=None)
    p24: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0, str]
    ] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = (
        pydantic.Field(alias="pay_by_bank", default=None)
    )
    payco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaycoObj0, str
        ]
    ] = pydantic.Field(alias="payco", default=None)
    paynow: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaynowObj0, str
        ]
    ] = pydantic.Field(alias="paynow", default=None)
    paypal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPaypalObj0, str
        ]
    ] = pydantic.Field(alias="paypal", default=None)
    pix: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPixObj0, str]
    ] = pydantic.Field(alias="pix", default=None)
    promptpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsPromptpayObj0, str
        ]
    ] = pydantic.Field(alias="promptpay", default=None)
    revolut_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsRevolutPayObj0, str
        ]
    ] = pydantic.Field(alias="revolut_pay", default=None)
    samsung_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSamsungPayObj0, str
        ]
    ] = pydantic.Field(alias="samsung_pay", default=None)
    sepa_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0, str
        ]
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSofortObj0, str
        ]
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0, str
        ]
    ] = pydantic.Field(alias="swish", default=None)
    twint: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0, str
        ]
    ] = pydantic.Field(alias="twint", default=None)
    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0, str
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsWechatPayObj0, str
        ]
    ] = pydantic.Field(alias="wechat_pay", default=None)
    zip: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyPaymentMethodOptionsZipObj0, str]
    ] = pydantic.Field(alias="zip", default=None)
