import pydantic
import typing
import typing_extensions

from .account_create_body_capabilities_acss_debit_payments import (
    AccountCreateBodyCapabilitiesAcssDebitPayments,
    _SerializerAccountCreateBodyCapabilitiesAcssDebitPayments,
)
from .account_create_body_capabilities_affirm_payments import (
    AccountCreateBodyCapabilitiesAffirmPayments,
    _SerializerAccountCreateBodyCapabilitiesAffirmPayments,
)
from .account_create_body_capabilities_afterpay_clearpay_payments import (
    AccountCreateBodyCapabilitiesAfterpayClearpayPayments,
    _SerializerAccountCreateBodyCapabilitiesAfterpayClearpayPayments,
)
from .account_create_body_capabilities_alma_payments import (
    AccountCreateBodyCapabilitiesAlmaPayments,
    _SerializerAccountCreateBodyCapabilitiesAlmaPayments,
)
from .account_create_body_capabilities_amazon_pay_payments import (
    AccountCreateBodyCapabilitiesAmazonPayPayments,
    _SerializerAccountCreateBodyCapabilitiesAmazonPayPayments,
)
from .account_create_body_capabilities_au_becs_debit_payments import (
    AccountCreateBodyCapabilitiesAuBecsDebitPayments,
    _SerializerAccountCreateBodyCapabilitiesAuBecsDebitPayments,
)
from .account_create_body_capabilities_bacs_debit_payments import (
    AccountCreateBodyCapabilitiesBacsDebitPayments,
    _SerializerAccountCreateBodyCapabilitiesBacsDebitPayments,
)
from .account_create_body_capabilities_bancontact_payments import (
    AccountCreateBodyCapabilitiesBancontactPayments,
    _SerializerAccountCreateBodyCapabilitiesBancontactPayments,
)
from .account_create_body_capabilities_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesBankTransferPayments,
)
from .account_create_body_capabilities_billie_payments import (
    AccountCreateBodyCapabilitiesBilliePayments,
    _SerializerAccountCreateBodyCapabilitiesBilliePayments,
)
from .account_create_body_capabilities_blik_payments import (
    AccountCreateBodyCapabilitiesBlikPayments,
    _SerializerAccountCreateBodyCapabilitiesBlikPayments,
)
from .account_create_body_capabilities_boleto_payments import (
    AccountCreateBodyCapabilitiesBoletoPayments,
    _SerializerAccountCreateBodyCapabilitiesBoletoPayments,
)
from .account_create_body_capabilities_card_issuing import (
    AccountCreateBodyCapabilitiesCardIssuing,
    _SerializerAccountCreateBodyCapabilitiesCardIssuing,
)
from .account_create_body_capabilities_card_payments import (
    AccountCreateBodyCapabilitiesCardPayments,
    _SerializerAccountCreateBodyCapabilitiesCardPayments,
)
from .account_create_body_capabilities_cartes_bancaires_payments import (
    AccountCreateBodyCapabilitiesCartesBancairesPayments,
    _SerializerAccountCreateBodyCapabilitiesCartesBancairesPayments,
)
from .account_create_body_capabilities_cashapp_payments import (
    AccountCreateBodyCapabilitiesCashappPayments,
    _SerializerAccountCreateBodyCapabilitiesCashappPayments,
)
from .account_create_body_capabilities_eps_payments import (
    AccountCreateBodyCapabilitiesEpsPayments,
    _SerializerAccountCreateBodyCapabilitiesEpsPayments,
)
from .account_create_body_capabilities_fpx_payments import (
    AccountCreateBodyCapabilitiesFpxPayments,
    _SerializerAccountCreateBodyCapabilitiesFpxPayments,
)
from .account_create_body_capabilities_gb_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesGbBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesGbBankTransferPayments,
)
from .account_create_body_capabilities_giropay_payments import (
    AccountCreateBodyCapabilitiesGiropayPayments,
    _SerializerAccountCreateBodyCapabilitiesGiropayPayments,
)
from .account_create_body_capabilities_grabpay_payments import (
    AccountCreateBodyCapabilitiesGrabpayPayments,
    _SerializerAccountCreateBodyCapabilitiesGrabpayPayments,
)
from .account_create_body_capabilities_ideal_payments import (
    AccountCreateBodyCapabilitiesIdealPayments,
    _SerializerAccountCreateBodyCapabilitiesIdealPayments,
)
from .account_create_body_capabilities_india_international_payments import (
    AccountCreateBodyCapabilitiesIndiaInternationalPayments,
    _SerializerAccountCreateBodyCapabilitiesIndiaInternationalPayments,
)
from .account_create_body_capabilities_jcb_payments import (
    AccountCreateBodyCapabilitiesJcbPayments,
    _SerializerAccountCreateBodyCapabilitiesJcbPayments,
)
from .account_create_body_capabilities_jp_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesJpBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesJpBankTransferPayments,
)
from .account_create_body_capabilities_kakao_pay_payments import (
    AccountCreateBodyCapabilitiesKakaoPayPayments,
    _SerializerAccountCreateBodyCapabilitiesKakaoPayPayments,
)
from .account_create_body_capabilities_klarna_payments import (
    AccountCreateBodyCapabilitiesKlarnaPayments,
    _SerializerAccountCreateBodyCapabilitiesKlarnaPayments,
)
from .account_create_body_capabilities_konbini_payments import (
    AccountCreateBodyCapabilitiesKonbiniPayments,
    _SerializerAccountCreateBodyCapabilitiesKonbiniPayments,
)
from .account_create_body_capabilities_kr_card_payments import (
    AccountCreateBodyCapabilitiesKrCardPayments,
    _SerializerAccountCreateBodyCapabilitiesKrCardPayments,
)
from .account_create_body_capabilities_legacy_payments import (
    AccountCreateBodyCapabilitiesLegacyPayments,
    _SerializerAccountCreateBodyCapabilitiesLegacyPayments,
)
from .account_create_body_capabilities_link_payments import (
    AccountCreateBodyCapabilitiesLinkPayments,
    _SerializerAccountCreateBodyCapabilitiesLinkPayments,
)
from .account_create_body_capabilities_mobilepay_payments import (
    AccountCreateBodyCapabilitiesMobilepayPayments,
    _SerializerAccountCreateBodyCapabilitiesMobilepayPayments,
)
from .account_create_body_capabilities_multibanco_payments import (
    AccountCreateBodyCapabilitiesMultibancoPayments,
    _SerializerAccountCreateBodyCapabilitiesMultibancoPayments,
)
from .account_create_body_capabilities_mx_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesMxBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesMxBankTransferPayments,
)
from .account_create_body_capabilities_naver_pay_payments import (
    AccountCreateBodyCapabilitiesNaverPayPayments,
    _SerializerAccountCreateBodyCapabilitiesNaverPayPayments,
)
from .account_create_body_capabilities_oxxo_payments import (
    AccountCreateBodyCapabilitiesOxxoPayments,
    _SerializerAccountCreateBodyCapabilitiesOxxoPayments,
)
from .account_create_body_capabilities_p24_payments import (
    AccountCreateBodyCapabilitiesP24Payments,
    _SerializerAccountCreateBodyCapabilitiesP24Payments,
)
from .account_create_body_capabilities_pay_by_bank_payments import (
    AccountCreateBodyCapabilitiesPayByBankPayments,
    _SerializerAccountCreateBodyCapabilitiesPayByBankPayments,
)
from .account_create_body_capabilities_payco_payments import (
    AccountCreateBodyCapabilitiesPaycoPayments,
    _SerializerAccountCreateBodyCapabilitiesPaycoPayments,
)
from .account_create_body_capabilities_paynow_payments import (
    AccountCreateBodyCapabilitiesPaynowPayments,
    _SerializerAccountCreateBodyCapabilitiesPaynowPayments,
)
from .account_create_body_capabilities_promptpay_payments import (
    AccountCreateBodyCapabilitiesPromptpayPayments,
    _SerializerAccountCreateBodyCapabilitiesPromptpayPayments,
)
from .account_create_body_capabilities_revolut_pay_payments import (
    AccountCreateBodyCapabilitiesRevolutPayPayments,
    _SerializerAccountCreateBodyCapabilitiesRevolutPayPayments,
)
from .account_create_body_capabilities_samsung_pay_payments import (
    AccountCreateBodyCapabilitiesSamsungPayPayments,
    _SerializerAccountCreateBodyCapabilitiesSamsungPayPayments,
)
from .account_create_body_capabilities_satispay_payments import (
    AccountCreateBodyCapabilitiesSatispayPayments,
    _SerializerAccountCreateBodyCapabilitiesSatispayPayments,
)
from .account_create_body_capabilities_sepa_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesSepaBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesSepaBankTransferPayments,
)
from .account_create_body_capabilities_sepa_debit_payments import (
    AccountCreateBodyCapabilitiesSepaDebitPayments,
    _SerializerAccountCreateBodyCapabilitiesSepaDebitPayments,
)
from .account_create_body_capabilities_sofort_payments import (
    AccountCreateBodyCapabilitiesSofortPayments,
    _SerializerAccountCreateBodyCapabilitiesSofortPayments,
)
from .account_create_body_capabilities_swish_payments import (
    AccountCreateBodyCapabilitiesSwishPayments,
    _SerializerAccountCreateBodyCapabilitiesSwishPayments,
)
from .account_create_body_capabilities_tax_reporting_us1099_k import (
    AccountCreateBodyCapabilitiesTaxReportingUs1099K,
    _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099K,
)
from .account_create_body_capabilities_tax_reporting_us1099_misc import (
    AccountCreateBodyCapabilitiesTaxReportingUs1099Misc,
    _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099Misc,
)
from .account_create_body_capabilities_transfers import (
    AccountCreateBodyCapabilitiesTransfers,
    _SerializerAccountCreateBodyCapabilitiesTransfers,
)
from .account_create_body_capabilities_treasury import (
    AccountCreateBodyCapabilitiesTreasury,
    _SerializerAccountCreateBodyCapabilitiesTreasury,
)
from .account_create_body_capabilities_twint_payments import (
    AccountCreateBodyCapabilitiesTwintPayments,
    _SerializerAccountCreateBodyCapabilitiesTwintPayments,
)
from .account_create_body_capabilities_us_bank_account_ach_payments import (
    AccountCreateBodyCapabilitiesUsBankAccountAchPayments,
    _SerializerAccountCreateBodyCapabilitiesUsBankAccountAchPayments,
)
from .account_create_body_capabilities_us_bank_transfer_payments import (
    AccountCreateBodyCapabilitiesUsBankTransferPayments,
    _SerializerAccountCreateBodyCapabilitiesUsBankTransferPayments,
)
from .account_create_body_capabilities_zip_payments import (
    AccountCreateBodyCapabilitiesZipPayments,
    _SerializerAccountCreateBodyCapabilitiesZipPayments,
)


class AccountCreateBodyCapabilities(typing_extensions.TypedDict):
    """
    Each key of the dictionary represents a capability, and each capability
    maps to its settings (for example, whether it has been requested or not). Each
    capability is inactive until you have provided its specific
    requirements and Stripe has verified them. An account might have some
    of its requested capabilities be active and some be inactive.

    Required when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)
    is `none`, which includes Custom accounts.
    """

    acss_debit_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAcssDebitPayments
    ]

    affirm_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAffirmPayments
    ]

    afterpay_clearpay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAfterpayClearpayPayments
    ]

    alma_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAlmaPayments
    ]

    amazon_pay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAmazonPayPayments
    ]

    au_becs_debit_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesAuBecsDebitPayments
    ]

    bacs_debit_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBacsDebitPayments
    ]

    bancontact_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBancontactPayments
    ]

    bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBankTransferPayments
    ]

    billie_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBilliePayments
    ]

    blik_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBlikPayments
    ]

    boleto_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesBoletoPayments
    ]

    card_issuing: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesCardIssuing
    ]

    card_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesCardPayments
    ]

    cartes_bancaires_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesCartesBancairesPayments
    ]

    cashapp_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesCashappPayments
    ]

    eps_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesEpsPayments
    ]

    fpx_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesFpxPayments
    ]

    gb_bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesGbBankTransferPayments
    ]

    giropay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesGiropayPayments
    ]

    grabpay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesGrabpayPayments
    ]

    ideal_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesIdealPayments
    ]

    india_international_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesIndiaInternationalPayments
    ]

    jcb_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesJcbPayments
    ]

    jp_bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesJpBankTransferPayments
    ]

    kakao_pay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesKakaoPayPayments
    ]

    klarna_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesKlarnaPayments
    ]

    konbini_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesKonbiniPayments
    ]

    kr_card_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesKrCardPayments
    ]

    legacy_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesLegacyPayments
    ]

    link_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesLinkPayments
    ]

    mobilepay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesMobilepayPayments
    ]

    multibanco_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesMultibancoPayments
    ]

    mx_bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesMxBankTransferPayments
    ]

    naver_pay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesNaverPayPayments
    ]

    oxxo_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesOxxoPayments
    ]

    p24_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesP24Payments
    ]

    pay_by_bank_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesPayByBankPayments
    ]

    payco_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesPaycoPayments
    ]

    paynow_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesPaynowPayments
    ]

    promptpay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesPromptpayPayments
    ]

    revolut_pay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesRevolutPayPayments
    ]

    samsung_pay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSamsungPayPayments
    ]

    satispay_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSatispayPayments
    ]

    sepa_bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSepaBankTransferPayments
    ]

    sepa_debit_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSepaDebitPayments
    ]

    sofort_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSofortPayments
    ]

    swish_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesSwishPayments
    ]

    tax_reporting_us_1099_k: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesTaxReportingUs1099K
    ]

    tax_reporting_us_1099_misc: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesTaxReportingUs1099Misc
    ]

    transfers: typing_extensions.NotRequired[AccountCreateBodyCapabilitiesTransfers]

    treasury: typing_extensions.NotRequired[AccountCreateBodyCapabilitiesTreasury]

    twint_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesTwintPayments
    ]

    us_bank_account_ach_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesUsBankAccountAchPayments
    ]

    us_bank_transfer_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesUsBankTransferPayments
    ]

    zip_payments: typing_extensions.NotRequired[
        AccountCreateBodyCapabilitiesZipPayments
    ]


class _SerializerAccountCreateBodyCapabilities(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilities handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAcssDebitPayments
    ] = pydantic.Field(alias="acss_debit_payments", default=None)
    affirm_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAffirmPayments
    ] = pydantic.Field(alias="affirm_payments", default=None)
    afterpay_clearpay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAfterpayClearpayPayments
    ] = pydantic.Field(alias="afterpay_clearpay_payments", default=None)
    alma_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAlmaPayments
    ] = pydantic.Field(alias="alma_payments", default=None)
    amazon_pay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAmazonPayPayments
    ] = pydantic.Field(alias="amazon_pay_payments", default=None)
    au_becs_debit_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesAuBecsDebitPayments
    ] = pydantic.Field(alias="au_becs_debit_payments", default=None)
    bacs_debit_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBacsDebitPayments
    ] = pydantic.Field(alias="bacs_debit_payments", default=None)
    bancontact_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBancontactPayments
    ] = pydantic.Field(alias="bancontact_payments", default=None)
    bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBankTransferPayments
    ] = pydantic.Field(alias="bank_transfer_payments", default=None)
    billie_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBilliePayments
    ] = pydantic.Field(alias="billie_payments", default=None)
    blik_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBlikPayments
    ] = pydantic.Field(alias="blik_payments", default=None)
    boleto_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesBoletoPayments
    ] = pydantic.Field(alias="boleto_payments", default=None)
    card_issuing: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    card_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesCardPayments
    ] = pydantic.Field(alias="card_payments", default=None)
    cartes_bancaires_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesCartesBancairesPayments
    ] = pydantic.Field(alias="cartes_bancaires_payments", default=None)
    cashapp_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesCashappPayments
    ] = pydantic.Field(alias="cashapp_payments", default=None)
    eps_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesEpsPayments
    ] = pydantic.Field(alias="eps_payments", default=None)
    fpx_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesFpxPayments
    ] = pydantic.Field(alias="fpx_payments", default=None)
    gb_bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesGbBankTransferPayments
    ] = pydantic.Field(alias="gb_bank_transfer_payments", default=None)
    giropay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesGiropayPayments
    ] = pydantic.Field(alias="giropay_payments", default=None)
    grabpay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesGrabpayPayments
    ] = pydantic.Field(alias="grabpay_payments", default=None)
    ideal_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesIdealPayments
    ] = pydantic.Field(alias="ideal_payments", default=None)
    india_international_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesIndiaInternationalPayments
    ] = pydantic.Field(alias="india_international_payments", default=None)
    jcb_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesJcbPayments
    ] = pydantic.Field(alias="jcb_payments", default=None)
    jp_bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesJpBankTransferPayments
    ] = pydantic.Field(alias="jp_bank_transfer_payments", default=None)
    kakao_pay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesKakaoPayPayments
    ] = pydantic.Field(alias="kakao_pay_payments", default=None)
    klarna_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesKlarnaPayments
    ] = pydantic.Field(alias="klarna_payments", default=None)
    konbini_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesKonbiniPayments
    ] = pydantic.Field(alias="konbini_payments", default=None)
    kr_card_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesKrCardPayments
    ] = pydantic.Field(alias="kr_card_payments", default=None)
    legacy_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesLegacyPayments
    ] = pydantic.Field(alias="legacy_payments", default=None)
    link_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesLinkPayments
    ] = pydantic.Field(alias="link_payments", default=None)
    mobilepay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesMobilepayPayments
    ] = pydantic.Field(alias="mobilepay_payments", default=None)
    multibanco_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesMultibancoPayments
    ] = pydantic.Field(alias="multibanco_payments", default=None)
    mx_bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesMxBankTransferPayments
    ] = pydantic.Field(alias="mx_bank_transfer_payments", default=None)
    naver_pay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesNaverPayPayments
    ] = pydantic.Field(alias="naver_pay_payments", default=None)
    oxxo_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesOxxoPayments
    ] = pydantic.Field(alias="oxxo_payments", default=None)
    p24_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesP24Payments
    ] = pydantic.Field(alias="p24_payments", default=None)
    pay_by_bank_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesPayByBankPayments
    ] = pydantic.Field(alias="pay_by_bank_payments", default=None)
    payco_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesPaycoPayments
    ] = pydantic.Field(alias="payco_payments", default=None)
    paynow_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesPaynowPayments
    ] = pydantic.Field(alias="paynow_payments", default=None)
    promptpay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesPromptpayPayments
    ] = pydantic.Field(alias="promptpay_payments", default=None)
    revolut_pay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesRevolutPayPayments
    ] = pydantic.Field(alias="revolut_pay_payments", default=None)
    samsung_pay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSamsungPayPayments
    ] = pydantic.Field(alias="samsung_pay_payments", default=None)
    satispay_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSatispayPayments
    ] = pydantic.Field(alias="satispay_payments", default=None)
    sepa_bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSepaBankTransferPayments
    ] = pydantic.Field(alias="sepa_bank_transfer_payments", default=None)
    sepa_debit_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSepaDebitPayments
    ] = pydantic.Field(alias="sepa_debit_payments", default=None)
    sofort_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSofortPayments
    ] = pydantic.Field(alias="sofort_payments", default=None)
    swish_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesSwishPayments
    ] = pydantic.Field(alias="swish_payments", default=None)
    tax_reporting_us_1099_k: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099K
    ] = pydantic.Field(alias="tax_reporting_us_1099_k", default=None)
    tax_reporting_us_1099_misc: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099Misc
    ] = pydantic.Field(alias="tax_reporting_us_1099_misc", default=None)
    transfers: typing.Optional[_SerializerAccountCreateBodyCapabilitiesTransfers] = (
        pydantic.Field(alias="transfers", default=None)
    )
    treasury: typing.Optional[_SerializerAccountCreateBodyCapabilitiesTreasury] = (
        pydantic.Field(alias="treasury", default=None)
    )
    twint_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesTwintPayments
    ] = pydantic.Field(alias="twint_payments", default=None)
    us_bank_account_ach_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesUsBankAccountAchPayments
    ] = pydantic.Field(alias="us_bank_account_ach_payments", default=None)
    us_bank_transfer_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesUsBankTransferPayments
    ] = pydantic.Field(alias="us_bank_transfer_payments", default=None)
    zip_payments: typing.Optional[
        _SerializerAccountCreateBodyCapabilitiesZipPayments
    ] = pydantic.Field(alias="zip_payments", default=None)
