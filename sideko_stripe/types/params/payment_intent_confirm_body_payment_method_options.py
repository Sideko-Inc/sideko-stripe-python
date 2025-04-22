import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_acss_debit_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0,
)
from .payment_intent_confirm_body_payment_method_options_affirm_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAffirmObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAffirmObj0,
)
from .payment_intent_confirm_body_payment_method_options_afterpay_clearpay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0,
)
from .payment_intent_confirm_body_payment_method_options_alipay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAlipayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAlipayObj0,
)
from .payment_intent_confirm_body_payment_method_options_alma_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAlmaObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAlmaObj0,
)
from .payment_intent_confirm_body_payment_method_options_amazon_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAmazonPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAmazonPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_au_becs_debit_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAuBecsDebitObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAuBecsDebitObj0,
)
from .payment_intent_confirm_body_payment_method_options_bacs_debit_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsBacsDebitObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBacsDebitObj0,
)
from .payment_intent_confirm_body_payment_method_options_bancontact_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0,
)
from .payment_intent_confirm_body_payment_method_options_blik_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0,
)
from .payment_intent_confirm_body_payment_method_options_boleto_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsBoletoObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBoletoObj0,
)
from .payment_intent_confirm_body_payment_method_options_card_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0,
)
from .payment_intent_confirm_body_payment_method_options_card_present_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0,
)
from .payment_intent_confirm_body_payment_method_options_cashapp_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCashappObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCashappObj0,
)
from .payment_intent_confirm_body_payment_method_options_customer_balance_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0,
)
from .payment_intent_confirm_body_payment_method_options_eps_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsEpsObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsEpsObj0,
)
from .payment_intent_confirm_body_payment_method_options_fpx_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsFpxObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsFpxObj0,
)
from .payment_intent_confirm_body_payment_method_options_giropay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsGiropayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsGiropayObj0,
)
from .payment_intent_confirm_body_payment_method_options_grabpay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsGrabpayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsGrabpayObj0,
)
from .payment_intent_confirm_body_payment_method_options_ideal_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0,
)
from .payment_intent_confirm_body_payment_method_options_kakao_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsKakaoPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKakaoPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_klarna_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsKlarnaObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKlarnaObj0,
)
from .payment_intent_confirm_body_payment_method_options_konbini_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsKonbiniObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKonbiniObj0,
)
from .payment_intent_confirm_body_payment_method_options_kr_card_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsKrCardObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKrCardObj0,
)
from .payment_intent_confirm_body_payment_method_options_link_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsLinkObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsLinkObj0,
)
from .payment_intent_confirm_body_payment_method_options_mobilepay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsMobilepayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsMobilepayObj0,
)
from .payment_intent_confirm_body_payment_method_options_multibanco_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsMultibancoObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsMultibancoObj0,
)
from .payment_intent_confirm_body_payment_method_options_naver_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsNaverPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsNaverPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_nz_bank_account_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsNzBankAccountObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsNzBankAccountObj0,
)
from .payment_intent_confirm_body_payment_method_options_oxxo_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0,
)
from .payment_intent_confirm_body_payment_method_options_p24_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsP24Obj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsP24Obj0,
)
from .payment_intent_confirm_body_payment_method_options_payco_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsPaycoObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaycoObj0,
)
from .payment_intent_confirm_body_payment_method_options_paynow_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsPaynowObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaynowObj0,
)
from .payment_intent_confirm_body_payment_method_options_paypal_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0,
)
from .payment_intent_confirm_body_payment_method_options_pix_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsPixObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPixObj0,
)
from .payment_intent_confirm_body_payment_method_options_promptpay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsPromptpayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPromptpayObj0,
)
from .payment_intent_confirm_body_payment_method_options_revolut_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_samsung_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsSamsungPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSamsungPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_sepa_debit_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsSepaDebitObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSepaDebitObj0,
)
from .payment_intent_confirm_body_payment_method_options_sofort_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsSofortObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSofortObj0,
)
from .payment_intent_confirm_body_payment_method_options_swish_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsSwishObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSwishObj0,
)
from .payment_intent_confirm_body_payment_method_options_twint_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsTwintObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsTwintObj0,
)
from .payment_intent_confirm_body_payment_method_options_us_bank_account_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0,
)
from .payment_intent_confirm_body_payment_method_options_wechat_pay_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsWechatPayObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsWechatPayObj0,
)
from .payment_intent_confirm_body_payment_method_options_zip_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsZipObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsZipObj0,
)


class PaymentIntentConfirmBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment method-specific configuration for this PaymentIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0, str]
    ]

    affirm: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAffirmObj0, str]
    ]

    afterpay_clearpay: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0, str
        ]
    ]

    alipay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAlipayObj0, str]
    ]

    alma: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAlmaObj0, str]
    ]

    amazon_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAmazonPayObj0, str]
    ]

    au_becs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsAuBecsDebitObj0, str]
    ]

    bacs_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsBacsDebitObj0, str]
    ]

    bancontact: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0, str]
    ]

    blik: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0, str]
    ]

    boleto: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsBoletoObj0, str]
    ]

    card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0, str]
    ]

    card_present: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0, str]
    ]

    cashapp: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsCashappObj0, str]
    ]

    customer_balance: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0, str
        ]
    ]

    eps: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsEpsObj0, str]
    ]

    fpx: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsFpxObj0, str]
    ]

    giropay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsGiropayObj0, str]
    ]

    grabpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsGrabpayObj0, str]
    ]

    ideal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0, str]
    ]

    interac_present: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    kakao_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsKakaoPayObj0, str]
    ]

    klarna: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsKlarnaObj0, str]
    ]

    konbini: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsKonbiniObj0, str]
    ]

    kr_card: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsKrCardObj0, str]
    ]

    link: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsLinkObj0, str]
    ]

    mobilepay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsMobilepayObj0, str]
    ]

    multibanco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsMultibancoObj0, str]
    ]

    naver_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsNaverPayObj0, str]
    ]

    nz_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsNzBankAccountObj0, str]
    ]

    oxxo: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0, str]
    ]

    p24: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsP24Obj0, str]
    ]

    pay_by_bank: typing_extensions.NotRequired[
        typing.Union[typing.Dict[str, typing.Any], str]
    ]

    payco: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsPaycoObj0, str]
    ]

    paynow: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsPaynowObj0, str]
    ]

    paypal: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0, str]
    ]

    pix: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsPixObj0, str]
    ]

    promptpay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsPromptpayObj0, str]
    ]

    revolut_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0, str]
    ]

    samsung_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsSamsungPayObj0, str]
    ]

    sepa_debit: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsSepaDebitObj0, str]
    ]

    sofort: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsSofortObj0, str]
    ]

    swish: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsSwishObj0, str]
    ]

    twint: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsTwintObj0, str]
    ]

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0, str]
    ]

    wechat_pay: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsWechatPayObj0, str]
    ]

    zip: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyPaymentMethodOptionsZipObj0, str]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0, str
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    affirm: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAffirmObj0, str
        ]
    ] = pydantic.Field(alias="affirm", default=None)
    afterpay_clearpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0,
            str,
        ]
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAlipayObj0, str
        ]
    ] = pydantic.Field(alias="alipay", default=None)
    alma: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAlmaObj0, str
        ]
    ] = pydantic.Field(alias="alma", default=None)
    amazon_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAmazonPayObj0, str
        ]
    ] = pydantic.Field(alias="amazon_pay", default=None)
    au_becs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAuBecsDebitObj0, str
        ]
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBacsDebitObj0, str
        ]
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0, str
        ]
    ] = pydantic.Field(alias="bancontact", default=None)
    blik: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBlikObj0, str
        ]
    ] = pydantic.Field(alias="blik", default=None)
    boleto: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBoletoObj0, str
        ]
    ] = pydantic.Field(alias="boleto", default=None)
    card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0, str
        ]
    ] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0, str
        ]
    ] = pydantic.Field(alias="card_present", default=None)
    cashapp: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCashappObj0, str
        ]
    ] = pydantic.Field(alias="cashapp", default=None)
    customer_balance: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0,
            str,
        ]
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsEpsObj0, str
        ]
    ] = pydantic.Field(alias="eps", default=None)
    fpx: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsFpxObj0, str
        ]
    ] = pydantic.Field(alias="fpx", default=None)
    giropay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsGiropayObj0, str
        ]
    ] = pydantic.Field(alias="giropay", default=None)
    grabpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsGrabpayObj0, str
        ]
    ] = pydantic.Field(alias="grabpay", default=None)
    ideal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsIdealObj0, str
        ]
    ] = pydantic.Field(alias="ideal", default=None)
    interac_present: typing.Optional[
        typing.Union[typing.Dict[str, typing.Any], str]
    ] = pydantic.Field(alias="interac_present", default=None)
    kakao_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKakaoPayObj0, str
        ]
    ] = pydantic.Field(alias="kakao_pay", default=None)
    klarna: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKlarnaObj0, str
        ]
    ] = pydantic.Field(alias="klarna", default=None)
    konbini: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKonbiniObj0, str
        ]
    ] = pydantic.Field(alias="konbini", default=None)
    kr_card: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsKrCardObj0, str
        ]
    ] = pydantic.Field(alias="kr_card", default=None)
    link: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsLinkObj0, str
        ]
    ] = pydantic.Field(alias="link", default=None)
    mobilepay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsMobilepayObj0, str
        ]
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsMultibancoObj0, str
        ]
    ] = pydantic.Field(alias="multibanco", default=None)
    naver_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsNaverPayObj0, str
        ]
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsNzBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsOxxoObj0, str
        ]
    ] = pydantic.Field(alias="oxxo", default=None)
    p24: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsP24Obj0, str
        ]
    ] = pydantic.Field(alias="p24", default=None)
    pay_by_bank: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = (
        pydantic.Field(alias="pay_by_bank", default=None)
    )
    payco: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaycoObj0, str
        ]
    ] = pydantic.Field(alias="payco", default=None)
    paynow: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaynowObj0, str
        ]
    ] = pydantic.Field(alias="paynow", default=None)
    paypal: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0, str
        ]
    ] = pydantic.Field(alias="paypal", default=None)
    pix: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPixObj0, str
        ]
    ] = pydantic.Field(alias="pix", default=None)
    promptpay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPromptpayObj0, str
        ]
    ] = pydantic.Field(alias="promptpay", default=None)
    revolut_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsRevolutPayObj0, str
        ]
    ] = pydantic.Field(alias="revolut_pay", default=None)
    samsung_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSamsungPayObj0, str
        ]
    ] = pydantic.Field(alias="samsung_pay", default=None)
    sepa_debit: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSepaDebitObj0, str
        ]
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSofortObj0, str
        ]
    ] = pydantic.Field(alias="sofort", default=None)
    swish: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsSwishObj0, str
        ]
    ] = pydantic.Field(alias="swish", default=None)
    twint: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsTwintObj0, str
        ]
    ] = pydantic.Field(alias="twint", default=None)
    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsWechatPayObj0, str
        ]
    ] = pydantic.Field(alias="wechat_pay", default=None)
    zip: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsZipObj0, str
        ]
    ] = pydantic.Field(alias="zip", default=None)
