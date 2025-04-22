import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_data_acss_debit import (
    SetupIntentUpdateBodyPaymentMethodDataAcssDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataAcssDebit,
)
from .setup_intent_update_body_payment_method_data_au_becs_debit import (
    SetupIntentUpdateBodyPaymentMethodDataAuBecsDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataAuBecsDebit,
)
from .setup_intent_update_body_payment_method_data_bacs_debit import (
    SetupIntentUpdateBodyPaymentMethodDataBacsDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataBacsDebit,
)
from .setup_intent_update_body_payment_method_data_billing_details import (
    SetupIntentUpdateBodyPaymentMethodDataBillingDetails,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataBillingDetails,
)
from .setup_intent_update_body_payment_method_data_boleto import (
    SetupIntentUpdateBodyPaymentMethodDataBoleto,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataBoleto,
)
from .setup_intent_update_body_payment_method_data_eps import (
    SetupIntentUpdateBodyPaymentMethodDataEps,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataEps,
)
from .setup_intent_update_body_payment_method_data_fpx import (
    SetupIntentUpdateBodyPaymentMethodDataFpx,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataFpx,
)
from .setup_intent_update_body_payment_method_data_ideal import (
    SetupIntentUpdateBodyPaymentMethodDataIdeal,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataIdeal,
)
from .setup_intent_update_body_payment_method_data_klarna import (
    SetupIntentUpdateBodyPaymentMethodDataKlarna,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataKlarna,
)
from .setup_intent_update_body_payment_method_data_metadata import (
    SetupIntentUpdateBodyPaymentMethodDataMetadata,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataMetadata,
)
from .setup_intent_update_body_payment_method_data_naver_pay import (
    SetupIntentUpdateBodyPaymentMethodDataNaverPay,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataNaverPay,
)
from .setup_intent_update_body_payment_method_data_nz_bank_account import (
    SetupIntentUpdateBodyPaymentMethodDataNzBankAccount,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataNzBankAccount,
)
from .setup_intent_update_body_payment_method_data_p24 import (
    SetupIntentUpdateBodyPaymentMethodDataP24,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataP24,
)
from .setup_intent_update_body_payment_method_data_radar_options import (
    SetupIntentUpdateBodyPaymentMethodDataRadarOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataRadarOptions,
)
from .setup_intent_update_body_payment_method_data_sepa_debit import (
    SetupIntentUpdateBodyPaymentMethodDataSepaDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataSepaDebit,
)
from .setup_intent_update_body_payment_method_data_sofort import (
    SetupIntentUpdateBodyPaymentMethodDataSofort,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataSofort,
)
from .setup_intent_update_body_payment_method_data_us_bank_account import (
    SetupIntentUpdateBodyPaymentMethodDataUsBankAccount,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataUsBankAccount,
)


class SetupIntentUpdateBodyPaymentMethodData(typing_extensions.TypedDict):
    """
    When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
    value in the SetupIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataAcssDebit
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
        SetupIntentUpdateBodyPaymentMethodDataAuBecsDebit
    ]

    bacs_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataBacsDebit
    ]

    bancontact: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    billie: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    billing_details: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataBillingDetails
    ]

    blik: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    boleto: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataBoleto]

    cashapp: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    customer_balance: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    eps: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataEps]

    fpx: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataFpx]

    giropay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    grabpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    ideal: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataIdeal]

    interac_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    kakao_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    klarna: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataKlarna]

    konbini: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    kr_card: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    metadata: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataMetadata
    ]

    mobilepay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    multibanco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    naver_pay: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataNaverPay
    ]

    nz_bank_account: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataNzBankAccount
    ]

    oxxo: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    p24: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataP24]

    pay_by_bank: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    payco: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paynow: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paypal: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    pix: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    promptpay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    radar_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataRadarOptions
    ]

    revolut_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    samsung_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    satispay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    sepa_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodDataSepaDebit
    ]

    sofort: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataSofort]

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
        SetupIntentUpdateBodyPaymentMethodDataUsBankAccount
    ]

    wechat_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    zip: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerSetupIntentUpdateBodyPaymentMethodData(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataAcssDebit
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
        _SerializerSetupIntentUpdateBodyPaymentMethodDataAuBecsDebit
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="bancontact", default=None
    )
    billie: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="billie", default=None
    )
    billing_details: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataBillingDetails
    ] = pydantic.Field(alias="billing_details", default=None)
    blik: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="blik", default=None
    )
    boleto: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataBoleto] = (
        pydantic.Field(alias="boleto", default=None)
    )
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer_balance: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="customer_balance", default=None
    )
    eps: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataEps] = (
        pydantic.Field(alias="eps", default=None)
    )
    fpx: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataFpx] = (
        pydantic.Field(alias="fpx", default=None)
    )
    giropay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="grabpay", default=None
    )
    ideal: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataIdeal] = (
        pydantic.Field(alias="ideal", default=None)
    )
    interac_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="interac_present", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataKlarna] = (
        pydantic.Field(alias="klarna", default=None)
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
    metadata: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    mobilepay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="mobilepay", default=None
    )
    multibanco: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="multibanco", default=None
    )
    naver_pay: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataNaverPay
    ] = pydantic.Field(alias="naver_pay", default=None)
    nz_bank_account: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodDataNzBankAccount
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="oxxo", default=None
    )
    p24: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataP24] = (
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
        _SerializerSetupIntentUpdateBodyPaymentMethodDataRadarOptions
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
        _SerializerSetupIntentUpdateBodyPaymentMethodDataSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataSofort] = (
        pydantic.Field(alias="sofort", default=None)
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
        _SerializerSetupIntentUpdateBodyPaymentMethodDataUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
