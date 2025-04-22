import pydantic
import typing
import typing_extensions

from .account_update_body_capabilities_acss_debit_payments import (
    AccountUpdateBodyCapabilitiesAcssDebitPayments,
    _SerializerAccountUpdateBodyCapabilitiesAcssDebitPayments,
)
from .account_update_body_capabilities_affirm_payments import (
    AccountUpdateBodyCapabilitiesAffirmPayments,
    _SerializerAccountUpdateBodyCapabilitiesAffirmPayments,
)
from .account_update_body_capabilities_afterpay_clearpay_payments import (
    AccountUpdateBodyCapabilitiesAfterpayClearpayPayments,
    _SerializerAccountUpdateBodyCapabilitiesAfterpayClearpayPayments,
)
from .account_update_body_capabilities_alma_payments import (
    AccountUpdateBodyCapabilitiesAlmaPayments,
    _SerializerAccountUpdateBodyCapabilitiesAlmaPayments,
)
from .account_update_body_capabilities_amazon_pay_payments import (
    AccountUpdateBodyCapabilitiesAmazonPayPayments,
    _SerializerAccountUpdateBodyCapabilitiesAmazonPayPayments,
)
from .account_update_body_capabilities_au_becs_debit_payments import (
    AccountUpdateBodyCapabilitiesAuBecsDebitPayments,
    _SerializerAccountUpdateBodyCapabilitiesAuBecsDebitPayments,
)
from .account_update_body_capabilities_bacs_debit_payments import (
    AccountUpdateBodyCapabilitiesBacsDebitPayments,
    _SerializerAccountUpdateBodyCapabilitiesBacsDebitPayments,
)
from .account_update_body_capabilities_bancontact_payments import (
    AccountUpdateBodyCapabilitiesBancontactPayments,
    _SerializerAccountUpdateBodyCapabilitiesBancontactPayments,
)
from .account_update_body_capabilities_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesBankTransferPayments,
)
from .account_update_body_capabilities_billie_payments import (
    AccountUpdateBodyCapabilitiesBilliePayments,
    _SerializerAccountUpdateBodyCapabilitiesBilliePayments,
)
from .account_update_body_capabilities_blik_payments import (
    AccountUpdateBodyCapabilitiesBlikPayments,
    _SerializerAccountUpdateBodyCapabilitiesBlikPayments,
)
from .account_update_body_capabilities_boleto_payments import (
    AccountUpdateBodyCapabilitiesBoletoPayments,
    _SerializerAccountUpdateBodyCapabilitiesBoletoPayments,
)
from .account_update_body_capabilities_card_issuing import (
    AccountUpdateBodyCapabilitiesCardIssuing,
    _SerializerAccountUpdateBodyCapabilitiesCardIssuing,
)
from .account_update_body_capabilities_card_payments import (
    AccountUpdateBodyCapabilitiesCardPayments,
    _SerializerAccountUpdateBodyCapabilitiesCardPayments,
)
from .account_update_body_capabilities_cartes_bancaires_payments import (
    AccountUpdateBodyCapabilitiesCartesBancairesPayments,
    _SerializerAccountUpdateBodyCapabilitiesCartesBancairesPayments,
)
from .account_update_body_capabilities_cashapp_payments import (
    AccountUpdateBodyCapabilitiesCashappPayments,
    _SerializerAccountUpdateBodyCapabilitiesCashappPayments,
)
from .account_update_body_capabilities_eps_payments import (
    AccountUpdateBodyCapabilitiesEpsPayments,
    _SerializerAccountUpdateBodyCapabilitiesEpsPayments,
)
from .account_update_body_capabilities_fpx_payments import (
    AccountUpdateBodyCapabilitiesFpxPayments,
    _SerializerAccountUpdateBodyCapabilitiesFpxPayments,
)
from .account_update_body_capabilities_gb_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesGbBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesGbBankTransferPayments,
)
from .account_update_body_capabilities_giropay_payments import (
    AccountUpdateBodyCapabilitiesGiropayPayments,
    _SerializerAccountUpdateBodyCapabilitiesGiropayPayments,
)
from .account_update_body_capabilities_grabpay_payments import (
    AccountUpdateBodyCapabilitiesGrabpayPayments,
    _SerializerAccountUpdateBodyCapabilitiesGrabpayPayments,
)
from .account_update_body_capabilities_ideal_payments import (
    AccountUpdateBodyCapabilitiesIdealPayments,
    _SerializerAccountUpdateBodyCapabilitiesIdealPayments,
)
from .account_update_body_capabilities_india_international_payments import (
    AccountUpdateBodyCapabilitiesIndiaInternationalPayments,
    _SerializerAccountUpdateBodyCapabilitiesIndiaInternationalPayments,
)
from .account_update_body_capabilities_jcb_payments import (
    AccountUpdateBodyCapabilitiesJcbPayments,
    _SerializerAccountUpdateBodyCapabilitiesJcbPayments,
)
from .account_update_body_capabilities_jp_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesJpBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesJpBankTransferPayments,
)
from .account_update_body_capabilities_kakao_pay_payments import (
    AccountUpdateBodyCapabilitiesKakaoPayPayments,
    _SerializerAccountUpdateBodyCapabilitiesKakaoPayPayments,
)
from .account_update_body_capabilities_klarna_payments import (
    AccountUpdateBodyCapabilitiesKlarnaPayments,
    _SerializerAccountUpdateBodyCapabilitiesKlarnaPayments,
)
from .account_update_body_capabilities_konbini_payments import (
    AccountUpdateBodyCapabilitiesKonbiniPayments,
    _SerializerAccountUpdateBodyCapabilitiesKonbiniPayments,
)
from .account_update_body_capabilities_kr_card_payments import (
    AccountUpdateBodyCapabilitiesKrCardPayments,
    _SerializerAccountUpdateBodyCapabilitiesKrCardPayments,
)
from .account_update_body_capabilities_legacy_payments import (
    AccountUpdateBodyCapabilitiesLegacyPayments,
    _SerializerAccountUpdateBodyCapabilitiesLegacyPayments,
)
from .account_update_body_capabilities_link_payments import (
    AccountUpdateBodyCapabilitiesLinkPayments,
    _SerializerAccountUpdateBodyCapabilitiesLinkPayments,
)
from .account_update_body_capabilities_mobilepay_payments import (
    AccountUpdateBodyCapabilitiesMobilepayPayments,
    _SerializerAccountUpdateBodyCapabilitiesMobilepayPayments,
)
from .account_update_body_capabilities_multibanco_payments import (
    AccountUpdateBodyCapabilitiesMultibancoPayments,
    _SerializerAccountUpdateBodyCapabilitiesMultibancoPayments,
)
from .account_update_body_capabilities_mx_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesMxBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesMxBankTransferPayments,
)
from .account_update_body_capabilities_naver_pay_payments import (
    AccountUpdateBodyCapabilitiesNaverPayPayments,
    _SerializerAccountUpdateBodyCapabilitiesNaverPayPayments,
)
from .account_update_body_capabilities_oxxo_payments import (
    AccountUpdateBodyCapabilitiesOxxoPayments,
    _SerializerAccountUpdateBodyCapabilitiesOxxoPayments,
)
from .account_update_body_capabilities_p24_payments import (
    AccountUpdateBodyCapabilitiesP24Payments,
    _SerializerAccountUpdateBodyCapabilitiesP24Payments,
)
from .account_update_body_capabilities_pay_by_bank_payments import (
    AccountUpdateBodyCapabilitiesPayByBankPayments,
    _SerializerAccountUpdateBodyCapabilitiesPayByBankPayments,
)
from .account_update_body_capabilities_payco_payments import (
    AccountUpdateBodyCapabilitiesPaycoPayments,
    _SerializerAccountUpdateBodyCapabilitiesPaycoPayments,
)
from .account_update_body_capabilities_paynow_payments import (
    AccountUpdateBodyCapabilitiesPaynowPayments,
    _SerializerAccountUpdateBodyCapabilitiesPaynowPayments,
)
from .account_update_body_capabilities_promptpay_payments import (
    AccountUpdateBodyCapabilitiesPromptpayPayments,
    _SerializerAccountUpdateBodyCapabilitiesPromptpayPayments,
)
from .account_update_body_capabilities_revolut_pay_payments import (
    AccountUpdateBodyCapabilitiesRevolutPayPayments,
    _SerializerAccountUpdateBodyCapabilitiesRevolutPayPayments,
)
from .account_update_body_capabilities_samsung_pay_payments import (
    AccountUpdateBodyCapabilitiesSamsungPayPayments,
    _SerializerAccountUpdateBodyCapabilitiesSamsungPayPayments,
)
from .account_update_body_capabilities_satispay_payments import (
    AccountUpdateBodyCapabilitiesSatispayPayments,
    _SerializerAccountUpdateBodyCapabilitiesSatispayPayments,
)
from .account_update_body_capabilities_sepa_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesSepaBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesSepaBankTransferPayments,
)
from .account_update_body_capabilities_sepa_debit_payments import (
    AccountUpdateBodyCapabilitiesSepaDebitPayments,
    _SerializerAccountUpdateBodyCapabilitiesSepaDebitPayments,
)
from .account_update_body_capabilities_sofort_payments import (
    AccountUpdateBodyCapabilitiesSofortPayments,
    _SerializerAccountUpdateBodyCapabilitiesSofortPayments,
)
from .account_update_body_capabilities_swish_payments import (
    AccountUpdateBodyCapabilitiesSwishPayments,
    _SerializerAccountUpdateBodyCapabilitiesSwishPayments,
)
from .account_update_body_capabilities_tax_reporting_us1099_k import (
    AccountUpdateBodyCapabilitiesTaxReportingUs1099K,
    _SerializerAccountUpdateBodyCapabilitiesTaxReportingUs1099K,
)
from .account_update_body_capabilities_tax_reporting_us1099_misc import (
    AccountUpdateBodyCapabilitiesTaxReportingUs1099Misc,
    _SerializerAccountUpdateBodyCapabilitiesTaxReportingUs1099Misc,
)
from .account_update_body_capabilities_transfers import (
    AccountUpdateBodyCapabilitiesTransfers,
    _SerializerAccountUpdateBodyCapabilitiesTransfers,
)
from .account_update_body_capabilities_treasury import (
    AccountUpdateBodyCapabilitiesTreasury,
    _SerializerAccountUpdateBodyCapabilitiesTreasury,
)
from .account_update_body_capabilities_twint_payments import (
    AccountUpdateBodyCapabilitiesTwintPayments,
    _SerializerAccountUpdateBodyCapabilitiesTwintPayments,
)
from .account_update_body_capabilities_us_bank_account_ach_payments import (
    AccountUpdateBodyCapabilitiesUsBankAccountAchPayments,
    _SerializerAccountUpdateBodyCapabilitiesUsBankAccountAchPayments,
)
from .account_update_body_capabilities_us_bank_transfer_payments import (
    AccountUpdateBodyCapabilitiesUsBankTransferPayments,
    _SerializerAccountUpdateBodyCapabilitiesUsBankTransferPayments,
)
from .account_update_body_capabilities_zip_payments import (
    AccountUpdateBodyCapabilitiesZipPayments,
    _SerializerAccountUpdateBodyCapabilitiesZipPayments,
)


class AccountUpdateBodyCapabilities(typing_extensions.TypedDict):
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
        AccountUpdateBodyCapabilitiesAcssDebitPayments
    ]

    affirm_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesAffirmPayments
    ]

    afterpay_clearpay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesAfterpayClearpayPayments
    ]

    alma_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesAlmaPayments
    ]

    amazon_pay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesAmazonPayPayments
    ]

    au_becs_debit_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesAuBecsDebitPayments
    ]

    bacs_debit_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBacsDebitPayments
    ]

    bancontact_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBancontactPayments
    ]

    bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBankTransferPayments
    ]

    billie_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBilliePayments
    ]

    blik_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBlikPayments
    ]

    boleto_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesBoletoPayments
    ]

    card_issuing: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesCardIssuing
    ]

    card_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesCardPayments
    ]

    cartes_bancaires_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesCartesBancairesPayments
    ]

    cashapp_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesCashappPayments
    ]

    eps_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesEpsPayments
    ]

    fpx_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesFpxPayments
    ]

    gb_bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesGbBankTransferPayments
    ]

    giropay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesGiropayPayments
    ]

    grabpay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesGrabpayPayments
    ]

    ideal_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesIdealPayments
    ]

    india_international_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesIndiaInternationalPayments
    ]

    jcb_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesJcbPayments
    ]

    jp_bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesJpBankTransferPayments
    ]

    kakao_pay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesKakaoPayPayments
    ]

    klarna_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesKlarnaPayments
    ]

    konbini_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesKonbiniPayments
    ]

    kr_card_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesKrCardPayments
    ]

    legacy_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesLegacyPayments
    ]

    link_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesLinkPayments
    ]

    mobilepay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesMobilepayPayments
    ]

    multibanco_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesMultibancoPayments
    ]

    mx_bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesMxBankTransferPayments
    ]

    naver_pay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesNaverPayPayments
    ]

    oxxo_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesOxxoPayments
    ]

    p24_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesP24Payments
    ]

    pay_by_bank_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesPayByBankPayments
    ]

    payco_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesPaycoPayments
    ]

    paynow_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesPaynowPayments
    ]

    promptpay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesPromptpayPayments
    ]

    revolut_pay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesRevolutPayPayments
    ]

    samsung_pay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSamsungPayPayments
    ]

    satispay_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSatispayPayments
    ]

    sepa_bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSepaBankTransferPayments
    ]

    sepa_debit_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSepaDebitPayments
    ]

    sofort_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSofortPayments
    ]

    swish_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesSwishPayments
    ]

    tax_reporting_us_1099_k: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesTaxReportingUs1099K
    ]

    tax_reporting_us_1099_misc: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesTaxReportingUs1099Misc
    ]

    transfers: typing_extensions.NotRequired[AccountUpdateBodyCapabilitiesTransfers]

    treasury: typing_extensions.NotRequired[AccountUpdateBodyCapabilitiesTreasury]

    twint_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesTwintPayments
    ]

    us_bank_account_ach_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesUsBankAccountAchPayments
    ]

    us_bank_transfer_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesUsBankTransferPayments
    ]

    zip_payments: typing_extensions.NotRequired[
        AccountUpdateBodyCapabilitiesZipPayments
    ]


class _SerializerAccountUpdateBodyCapabilities(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilities handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAcssDebitPayments
    ] = pydantic.Field(alias="acss_debit_payments", default=None)
    affirm_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAffirmPayments
    ] = pydantic.Field(alias="affirm_payments", default=None)
    afterpay_clearpay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAfterpayClearpayPayments
    ] = pydantic.Field(alias="afterpay_clearpay_payments", default=None)
    alma_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAlmaPayments
    ] = pydantic.Field(alias="alma_payments", default=None)
    amazon_pay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAmazonPayPayments
    ] = pydantic.Field(alias="amazon_pay_payments", default=None)
    au_becs_debit_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesAuBecsDebitPayments
    ] = pydantic.Field(alias="au_becs_debit_payments", default=None)
    bacs_debit_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBacsDebitPayments
    ] = pydantic.Field(alias="bacs_debit_payments", default=None)
    bancontact_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBancontactPayments
    ] = pydantic.Field(alias="bancontact_payments", default=None)
    bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBankTransferPayments
    ] = pydantic.Field(alias="bank_transfer_payments", default=None)
    billie_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBilliePayments
    ] = pydantic.Field(alias="billie_payments", default=None)
    blik_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBlikPayments
    ] = pydantic.Field(alias="blik_payments", default=None)
    boleto_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesBoletoPayments
    ] = pydantic.Field(alias="boleto_payments", default=None)
    card_issuing: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesCardIssuing
    ] = pydantic.Field(alias="card_issuing", default=None)
    card_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesCardPayments
    ] = pydantic.Field(alias="card_payments", default=None)
    cartes_bancaires_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesCartesBancairesPayments
    ] = pydantic.Field(alias="cartes_bancaires_payments", default=None)
    cashapp_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesCashappPayments
    ] = pydantic.Field(alias="cashapp_payments", default=None)
    eps_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesEpsPayments
    ] = pydantic.Field(alias="eps_payments", default=None)
    fpx_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesFpxPayments
    ] = pydantic.Field(alias="fpx_payments", default=None)
    gb_bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesGbBankTransferPayments
    ] = pydantic.Field(alias="gb_bank_transfer_payments", default=None)
    giropay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesGiropayPayments
    ] = pydantic.Field(alias="giropay_payments", default=None)
    grabpay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesGrabpayPayments
    ] = pydantic.Field(alias="grabpay_payments", default=None)
    ideal_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesIdealPayments
    ] = pydantic.Field(alias="ideal_payments", default=None)
    india_international_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesIndiaInternationalPayments
    ] = pydantic.Field(alias="india_international_payments", default=None)
    jcb_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesJcbPayments
    ] = pydantic.Field(alias="jcb_payments", default=None)
    jp_bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesJpBankTransferPayments
    ] = pydantic.Field(alias="jp_bank_transfer_payments", default=None)
    kakao_pay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesKakaoPayPayments
    ] = pydantic.Field(alias="kakao_pay_payments", default=None)
    klarna_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesKlarnaPayments
    ] = pydantic.Field(alias="klarna_payments", default=None)
    konbini_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesKonbiniPayments
    ] = pydantic.Field(alias="konbini_payments", default=None)
    kr_card_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesKrCardPayments
    ] = pydantic.Field(alias="kr_card_payments", default=None)
    legacy_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesLegacyPayments
    ] = pydantic.Field(alias="legacy_payments", default=None)
    link_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesLinkPayments
    ] = pydantic.Field(alias="link_payments", default=None)
    mobilepay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesMobilepayPayments
    ] = pydantic.Field(alias="mobilepay_payments", default=None)
    multibanco_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesMultibancoPayments
    ] = pydantic.Field(alias="multibanco_payments", default=None)
    mx_bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesMxBankTransferPayments
    ] = pydantic.Field(alias="mx_bank_transfer_payments", default=None)
    naver_pay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesNaverPayPayments
    ] = pydantic.Field(alias="naver_pay_payments", default=None)
    oxxo_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesOxxoPayments
    ] = pydantic.Field(alias="oxxo_payments", default=None)
    p24_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesP24Payments
    ] = pydantic.Field(alias="p24_payments", default=None)
    pay_by_bank_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesPayByBankPayments
    ] = pydantic.Field(alias="pay_by_bank_payments", default=None)
    payco_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesPaycoPayments
    ] = pydantic.Field(alias="payco_payments", default=None)
    paynow_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesPaynowPayments
    ] = pydantic.Field(alias="paynow_payments", default=None)
    promptpay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesPromptpayPayments
    ] = pydantic.Field(alias="promptpay_payments", default=None)
    revolut_pay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesRevolutPayPayments
    ] = pydantic.Field(alias="revolut_pay_payments", default=None)
    samsung_pay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSamsungPayPayments
    ] = pydantic.Field(alias="samsung_pay_payments", default=None)
    satispay_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSatispayPayments
    ] = pydantic.Field(alias="satispay_payments", default=None)
    sepa_bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSepaBankTransferPayments
    ] = pydantic.Field(alias="sepa_bank_transfer_payments", default=None)
    sepa_debit_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSepaDebitPayments
    ] = pydantic.Field(alias="sepa_debit_payments", default=None)
    sofort_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSofortPayments
    ] = pydantic.Field(alias="sofort_payments", default=None)
    swish_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesSwishPayments
    ] = pydantic.Field(alias="swish_payments", default=None)
    tax_reporting_us_1099_k: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesTaxReportingUs1099K
    ] = pydantic.Field(alias="tax_reporting_us_1099_k", default=None)
    tax_reporting_us_1099_misc: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesTaxReportingUs1099Misc
    ] = pydantic.Field(alias="tax_reporting_us_1099_misc", default=None)
    transfers: typing.Optional[_SerializerAccountUpdateBodyCapabilitiesTransfers] = (
        pydantic.Field(alias="transfers", default=None)
    )
    treasury: typing.Optional[_SerializerAccountUpdateBodyCapabilitiesTreasury] = (
        pydantic.Field(alias="treasury", default=None)
    )
    twint_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesTwintPayments
    ] = pydantic.Field(alias="twint_payments", default=None)
    us_bank_account_ach_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesUsBankAccountAchPayments
    ] = pydantic.Field(alias="us_bank_account_ach_payments", default=None)
    us_bank_transfer_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesUsBankTransferPayments
    ] = pydantic.Field(alias="us_bank_transfer_payments", default=None)
    zip_payments: typing.Optional[
        _SerializerAccountUpdateBodyCapabilitiesZipPayments
    ] = pydantic.Field(alias="zip_payments", default=None)
