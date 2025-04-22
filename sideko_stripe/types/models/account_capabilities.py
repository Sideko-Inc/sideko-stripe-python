import pydantic
import typing
import typing_extensions


class AccountCapabilities(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="acss_debit_payments", default=None)
    """
    The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges.
    """
    affirm_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="affirm_payments", default=None)
    """
    The status of the Affirm capability of the account, or whether the account can directly process Affirm charges.
    """
    afterpay_clearpay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="afterpay_clearpay_payments", default=None)
    """
    The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges.
    """
    alma_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="alma_payments", default=None)
    """
    The status of the Alma capability of the account, or whether the account can directly process Alma payments.
    """
    amazon_pay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="amazon_pay_payments", default=None)
    """
    The status of the AmazonPay capability of the account, or whether the account can directly process AmazonPay payments.
    """
    au_becs_debit_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="au_becs_debit_payments", default=None)
    """
    The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges.
    """
    bacs_debit_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="bacs_debit_payments", default=None)
    """
    The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges.
    """
    bancontact_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="bancontact_payments", default=None)
    """
    The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges.
    """
    bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="bank_transfer_payments", default=None)
    """
    The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges.
    """
    billie_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="billie_payments", default=None)
    """
    The status of the Billie capability of the account, or whether the account can directly process Billie payments.
    """
    blik_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="blik_payments", default=None)
    """
    The status of the blik payments capability of the account, or whether the account can directly process blik charges.
    """
    boleto_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="boleto_payments", default=None)
    """
    The status of the boleto payments capability of the account, or whether the account can directly process boleto charges.
    """
    card_issuing: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="card_issuing", default=None)
    """
    The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards
    """
    card_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="card_payments", default=None)
    """
    The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges.
    """
    cartes_bancaires_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="cartes_bancaires_payments", default=None)
    """
    The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency.
    """
    cashapp_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="cashapp_payments", default=None)
    """
    The status of the Cash App Pay capability of the account, or whether the account can directly process Cash App Pay payments.
    """
    eps_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="eps_payments", default=None)
    """
    The status of the EPS payments capability of the account, or whether the account can directly process EPS charges.
    """
    fpx_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="fpx_payments", default=None)
    """
    The status of the FPX payments capability of the account, or whether the account can directly process FPX charges.
    """
    gb_bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="gb_bank_transfer_payments", default=None)
    """
    The status of the GB customer_balance payments (GBP currency) capability of the account, or whether the account can directly process GB customer_balance charges.
    """
    giropay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="giropay_payments", default=None)
    """
    The status of the giropay payments capability of the account, or whether the account can directly process giropay charges.
    """
    grabpay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="grabpay_payments", default=None)
    """
    The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges.
    """
    ideal_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="ideal_payments", default=None)
    """
    The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges.
    """
    india_international_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="india_international_payments", default=None)
    """
    The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India.
    """
    jcb_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="jcb_payments", default=None)
    """
    The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency.
    """
    jp_bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="jp_bank_transfer_payments", default=None)
    """
    The status of the Japanese customer_balance payments (JPY currency) capability of the account, or whether the account can directly process Japanese customer_balance charges.
    """
    kakao_pay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="kakao_pay_payments", default=None)
    """
    The status of the KakaoPay capability of the account, or whether the account can directly process KakaoPay payments.
    """
    klarna_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="klarna_payments", default=None)
    """
    The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges.
    """
    konbini_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="konbini_payments", default=None)
    """
    The status of the konbini payments capability of the account, or whether the account can directly process konbini charges.
    """
    kr_card_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="kr_card_payments", default=None)
    """
    The status of the KrCard capability of the account, or whether the account can directly process KrCard payments.
    """
    legacy_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="legacy_payments", default=None)
    """
    The status of the legacy payments capability of the account.
    """
    link_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="link_payments", default=None)
    """
    The status of the link_payments capability of the account, or whether the account can directly process Link charges.
    """
    mobilepay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="mobilepay_payments", default=None)
    """
    The status of the MobilePay capability of the account, or whether the account can directly process MobilePay charges.
    """
    multibanco_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="multibanco_payments", default=None)
    """
    The status of the Multibanco payments capability of the account, or whether the account can directly process Multibanco charges.
    """
    mx_bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="mx_bank_transfer_payments", default=None)
    """
    The status of the Mexican customer_balance payments (MXN currency) capability of the account, or whether the account can directly process Mexican customer_balance charges.
    """
    naver_pay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="naver_pay_payments", default=None)
    """
    The status of the NaverPay capability of the account, or whether the account can directly process NaverPay payments.
    """
    oxxo_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="oxxo_payments", default=None)
    """
    The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges.
    """
    p24_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="p24_payments", default=None)
    """
    The status of the P24 payments capability of the account, or whether the account can directly process P24 charges.
    """
    pay_by_bank_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="pay_by_bank_payments", default=None)
    """
    The status of the pay_by_bank payments capability of the account, or whether the account can directly process pay_by_bank charges.
    """
    payco_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="payco_payments", default=None)
    """
    The status of the Payco capability of the account, or whether the account can directly process Payco payments.
    """
    paynow_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="paynow_payments", default=None)
    """
    The status of the paynow payments capability of the account, or whether the account can directly process paynow charges.
    """
    promptpay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="promptpay_payments", default=None)
    """
    The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges.
    """
    revolut_pay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="revolut_pay_payments", default=None)
    """
    The status of the RevolutPay capability of the account, or whether the account can directly process RevolutPay payments.
    """
    samsung_pay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="samsung_pay_payments", default=None)
    """
    The status of the SamsungPay capability of the account, or whether the account can directly process SamsungPay payments.
    """
    satispay_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="satispay_payments", default=None)
    """
    The status of the Satispay capability of the account, or whether the account can directly process Satispay payments.
    """
    sepa_bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="sepa_bank_transfer_payments", default=None)
    """
    The status of the SEPA customer_balance payments (EUR currency) capability of the account, or whether the account can directly process SEPA customer_balance charges.
    """
    sepa_debit_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="sepa_debit_payments", default=None)
    """
    The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges.
    """
    sofort_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="sofort_payments", default=None)
    """
    The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges.
    """
    swish_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="swish_payments", default=None)
    """
    The status of the Swish capability of the account, or whether the account can directly process Swish payments.
    """
    tax_reporting_us_1099_k: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="tax_reporting_us_1099_k", default=None)
    """
    The status of the tax reporting 1099-K (US) capability of the account.
    """
    tax_reporting_us_1099_misc: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="tax_reporting_us_1099_misc", default=None)
    """
    The status of the tax reporting 1099-MISC (US) capability of the account.
    """
    transfers: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="transfers", default=None)
    """
    The status of the transfers capability of the account, or whether your platform can transfer funds to the account.
    """
    treasury: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="treasury", default=None)
    """
    The status of the banking capability, or whether the account can have bank accounts.
    """
    twint_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="twint_payments", default=None)
    """
    The status of the TWINT capability of the account, or whether the account can directly process TWINT charges.
    """
    us_bank_account_ach_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="us_bank_account_ach_payments", default=None)
    """
    The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges.
    """
    us_bank_transfer_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="us_bank_transfer_payments", default=None)
    """
    The status of the US customer_balance payments (USD currency) capability of the account, or whether the account can directly process US customer_balance charges.
    """
    zip_payments: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="zip_payments", default=None)
    """
    The status of the Zip capability of the account, or whether the account can directly process Zip charges.
    """
