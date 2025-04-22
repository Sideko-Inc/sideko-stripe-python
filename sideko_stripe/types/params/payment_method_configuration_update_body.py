import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_acss_debit import (
    PaymentMethodConfigurationUpdateBodyAcssDebit,
    _SerializerPaymentMethodConfigurationUpdateBodyAcssDebit,
)
from .payment_method_configuration_update_body_affirm import (
    PaymentMethodConfigurationUpdateBodyAffirm,
    _SerializerPaymentMethodConfigurationUpdateBodyAffirm,
)
from .payment_method_configuration_update_body_afterpay_clearpay import (
    PaymentMethodConfigurationUpdateBodyAfterpayClearpay,
    _SerializerPaymentMethodConfigurationUpdateBodyAfterpayClearpay,
)
from .payment_method_configuration_update_body_alipay import (
    PaymentMethodConfigurationUpdateBodyAlipay,
    _SerializerPaymentMethodConfigurationUpdateBodyAlipay,
)
from .payment_method_configuration_update_body_alma import (
    PaymentMethodConfigurationUpdateBodyAlma,
    _SerializerPaymentMethodConfigurationUpdateBodyAlma,
)
from .payment_method_configuration_update_body_amazon_pay import (
    PaymentMethodConfigurationUpdateBodyAmazonPay,
    _SerializerPaymentMethodConfigurationUpdateBodyAmazonPay,
)
from .payment_method_configuration_update_body_apple_pay import (
    PaymentMethodConfigurationUpdateBodyApplePay,
    _SerializerPaymentMethodConfigurationUpdateBodyApplePay,
)
from .payment_method_configuration_update_body_apple_pay_later import (
    PaymentMethodConfigurationUpdateBodyApplePayLater,
    _SerializerPaymentMethodConfigurationUpdateBodyApplePayLater,
)
from .payment_method_configuration_update_body_au_becs_debit import (
    PaymentMethodConfigurationUpdateBodyAuBecsDebit,
    _SerializerPaymentMethodConfigurationUpdateBodyAuBecsDebit,
)
from .payment_method_configuration_update_body_bacs_debit import (
    PaymentMethodConfigurationUpdateBodyBacsDebit,
    _SerializerPaymentMethodConfigurationUpdateBodyBacsDebit,
)
from .payment_method_configuration_update_body_bancontact import (
    PaymentMethodConfigurationUpdateBodyBancontact,
    _SerializerPaymentMethodConfigurationUpdateBodyBancontact,
)
from .payment_method_configuration_update_body_billie import (
    PaymentMethodConfigurationUpdateBodyBillie,
    _SerializerPaymentMethodConfigurationUpdateBodyBillie,
)
from .payment_method_configuration_update_body_blik import (
    PaymentMethodConfigurationUpdateBodyBlik,
    _SerializerPaymentMethodConfigurationUpdateBodyBlik,
)
from .payment_method_configuration_update_body_boleto import (
    PaymentMethodConfigurationUpdateBodyBoleto,
    _SerializerPaymentMethodConfigurationUpdateBodyBoleto,
)
from .payment_method_configuration_update_body_card import (
    PaymentMethodConfigurationUpdateBodyCard,
    _SerializerPaymentMethodConfigurationUpdateBodyCard,
)
from .payment_method_configuration_update_body_cartes_bancaires import (
    PaymentMethodConfigurationUpdateBodyCartesBancaires,
    _SerializerPaymentMethodConfigurationUpdateBodyCartesBancaires,
)
from .payment_method_configuration_update_body_cashapp import (
    PaymentMethodConfigurationUpdateBodyCashapp,
    _SerializerPaymentMethodConfigurationUpdateBodyCashapp,
)
from .payment_method_configuration_update_body_customer_balance import (
    PaymentMethodConfigurationUpdateBodyCustomerBalance,
    _SerializerPaymentMethodConfigurationUpdateBodyCustomerBalance,
)
from .payment_method_configuration_update_body_eps import (
    PaymentMethodConfigurationUpdateBodyEps,
    _SerializerPaymentMethodConfigurationUpdateBodyEps,
)
from .payment_method_configuration_update_body_fpx import (
    PaymentMethodConfigurationUpdateBodyFpx,
    _SerializerPaymentMethodConfigurationUpdateBodyFpx,
)
from .payment_method_configuration_update_body_giropay import (
    PaymentMethodConfigurationUpdateBodyGiropay,
    _SerializerPaymentMethodConfigurationUpdateBodyGiropay,
)
from .payment_method_configuration_update_body_google_pay import (
    PaymentMethodConfigurationUpdateBodyGooglePay,
    _SerializerPaymentMethodConfigurationUpdateBodyGooglePay,
)
from .payment_method_configuration_update_body_grabpay import (
    PaymentMethodConfigurationUpdateBodyGrabpay,
    _SerializerPaymentMethodConfigurationUpdateBodyGrabpay,
)
from .payment_method_configuration_update_body_ideal import (
    PaymentMethodConfigurationUpdateBodyIdeal,
    _SerializerPaymentMethodConfigurationUpdateBodyIdeal,
)
from .payment_method_configuration_update_body_jcb import (
    PaymentMethodConfigurationUpdateBodyJcb,
    _SerializerPaymentMethodConfigurationUpdateBodyJcb,
)
from .payment_method_configuration_update_body_klarna import (
    PaymentMethodConfigurationUpdateBodyKlarna,
    _SerializerPaymentMethodConfigurationUpdateBodyKlarna,
)
from .payment_method_configuration_update_body_konbini import (
    PaymentMethodConfigurationUpdateBodyKonbini,
    _SerializerPaymentMethodConfigurationUpdateBodyKonbini,
)
from .payment_method_configuration_update_body_link import (
    PaymentMethodConfigurationUpdateBodyLink,
    _SerializerPaymentMethodConfigurationUpdateBodyLink,
)
from .payment_method_configuration_update_body_mobilepay import (
    PaymentMethodConfigurationUpdateBodyMobilepay,
    _SerializerPaymentMethodConfigurationUpdateBodyMobilepay,
)
from .payment_method_configuration_update_body_multibanco import (
    PaymentMethodConfigurationUpdateBodyMultibanco,
    _SerializerPaymentMethodConfigurationUpdateBodyMultibanco,
)
from .payment_method_configuration_update_body_nz_bank_account import (
    PaymentMethodConfigurationUpdateBodyNzBankAccount,
    _SerializerPaymentMethodConfigurationUpdateBodyNzBankAccount,
)
from .payment_method_configuration_update_body_oxxo import (
    PaymentMethodConfigurationUpdateBodyOxxo,
    _SerializerPaymentMethodConfigurationUpdateBodyOxxo,
)
from .payment_method_configuration_update_body_p24 import (
    PaymentMethodConfigurationUpdateBodyP24,
    _SerializerPaymentMethodConfigurationUpdateBodyP24,
)
from .payment_method_configuration_update_body_pay_by_bank import (
    PaymentMethodConfigurationUpdateBodyPayByBank,
    _SerializerPaymentMethodConfigurationUpdateBodyPayByBank,
)
from .payment_method_configuration_update_body_paynow import (
    PaymentMethodConfigurationUpdateBodyPaynow,
    _SerializerPaymentMethodConfigurationUpdateBodyPaynow,
)
from .payment_method_configuration_update_body_paypal import (
    PaymentMethodConfigurationUpdateBodyPaypal,
    _SerializerPaymentMethodConfigurationUpdateBodyPaypal,
)
from .payment_method_configuration_update_body_promptpay import (
    PaymentMethodConfigurationUpdateBodyPromptpay,
    _SerializerPaymentMethodConfigurationUpdateBodyPromptpay,
)
from .payment_method_configuration_update_body_revolut_pay import (
    PaymentMethodConfigurationUpdateBodyRevolutPay,
    _SerializerPaymentMethodConfigurationUpdateBodyRevolutPay,
)
from .payment_method_configuration_update_body_satispay import (
    PaymentMethodConfigurationUpdateBodySatispay,
    _SerializerPaymentMethodConfigurationUpdateBodySatispay,
)
from .payment_method_configuration_update_body_sepa_debit import (
    PaymentMethodConfigurationUpdateBodySepaDebit,
    _SerializerPaymentMethodConfigurationUpdateBodySepaDebit,
)
from .payment_method_configuration_update_body_sofort import (
    PaymentMethodConfigurationUpdateBodySofort,
    _SerializerPaymentMethodConfigurationUpdateBodySofort,
)
from .payment_method_configuration_update_body_swish import (
    PaymentMethodConfigurationUpdateBodySwish,
    _SerializerPaymentMethodConfigurationUpdateBodySwish,
)
from .payment_method_configuration_update_body_twint import (
    PaymentMethodConfigurationUpdateBodyTwint,
    _SerializerPaymentMethodConfigurationUpdateBodyTwint,
)
from .payment_method_configuration_update_body_us_bank_account import (
    PaymentMethodConfigurationUpdateBodyUsBankAccount,
    _SerializerPaymentMethodConfigurationUpdateBodyUsBankAccount,
)
from .payment_method_configuration_update_body_wechat_pay import (
    PaymentMethodConfigurationUpdateBodyWechatPay,
    _SerializerPaymentMethodConfigurationUpdateBodyWechatPay,
)
from .payment_method_configuration_update_body_zip import (
    PaymentMethodConfigurationUpdateBodyZip,
    _SerializerPaymentMethodConfigurationUpdateBodyZip,
)


class PaymentMethodConfigurationUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodConfigurationUpdateBody
    """

    acss_debit: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAcssDebit
    ]
    """
    Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the configuration can be used for new payments.
    """

    affirm: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyAffirm]
    """
    [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
    """

    afterpay_clearpay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAfterpayClearpay
    ]
    """
    Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
    """

    alipay: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyAlipay]
    """
    Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
    """

    alma: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyAlma]
    """
    Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.
    """

    amazon_pay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAmazonPay
    ]
    """
    Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.
    """

    apple_pay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyApplePay
    ]
    """
    Stripe users can accept [Apple Pay](/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
    """

    apple_pay_later: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyApplePayLater
    ]
    """
    Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
    """

    au_becs_debit: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAuBecsDebit
    ]
    """
    Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
    """

    bacs_debit: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBacsDebit
    ]
    """
    Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
    """

    bancontact: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBancontact
    ]
    """
    Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
    """

    billie: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyBillie]
    """
    Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    """

    blik: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyBlik]
    """
    BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
    """

    boleto: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyBoleto]
    """
    Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
    """

    card: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyCard]
    """
    Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
    """

    cartes_bancaires: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyCartesBancaires
    ]
    """
    Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
    """

    cashapp: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyCashapp]
    """
    Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
    """

    customer_balance: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyCustomerBalance
    ]
    """
    Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details.
    """

    eps: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyEps]
    """
    EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fpx: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyFpx]
    """
    Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
    """

    giropay: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyGiropay]
    """
    giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
    """

    google_pay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyGooglePay
    ]
    """
    Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
    """

    grabpay: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyGrabpay]
    """
    GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
    """

    ideal: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyIdeal]
    """
    iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
    """

    jcb: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyJcb]
    """
    JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
    """

    klarna: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyKlarna]
    """
    Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
    """

    konbini: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyKonbini]
    """
    Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
    """

    link: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyLink]
    """
    [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
    """

    mobilepay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyMobilepay
    ]
    """
    MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details.
    """

    multibanco: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyMultibanco
    ]
    """
    Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.
    """

    name: typing_extensions.NotRequired[str]
    """
    Configuration name.
    """

    nz_bank_account: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyNzBankAccount
    ]
    """
    Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details.
    """

    oxxo: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyOxxo]
    """
    OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
    """

    p24: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyP24]
    """
    Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
    """

    pay_by_bank: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyPayByBank
    ]
    """
    Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.
    """

    paynow: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyPaynow]
    """
    PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
    """

    paypal: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyPaypal]
    """
    PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
    """

    promptpay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyPromptpay
    ]
    """
    PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
    """

    revolut_pay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyRevolutPay
    ]
    """
    Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.
    """

    satispay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodySatispay
    ]
    """
    Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    """

    sepa_debit: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodySepaDebit
    ]
    """
    The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
    """

    sofort: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodySofort]
    """
    Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
    """

    swish: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodySwish]
    """
    Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details.
    """

    twint: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyTwint]
    """
    Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details.
    """

    us_bank_account: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyUsBankAccount
    ]
    """
    Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details.
    """

    wechat_pay: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyWechatPay
    ]
    """
    WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
    """

    zip: typing_extensions.NotRequired[PaymentMethodConfigurationUpdateBodyZip]
    """
    Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability.
    """


class _SerializerPaymentMethodConfigurationUpdateBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    acss_debit: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    affirm: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyAffirm] = (
        pydantic.Field(alias="affirm", default=None)
    )
    afterpay_clearpay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAfterpayClearpay
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyAlipay] = (
        pydantic.Field(alias="alipay", default=None)
    )
    alma: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyAlma] = (
        pydantic.Field(alias="alma", default=None)
    )
    amazon_pay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAmazonPay
    ] = pydantic.Field(alias="amazon_pay", default=None)
    apple_pay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyApplePay
    ] = pydantic.Field(alias="apple_pay", default=None)
    apple_pay_later: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyApplePayLater
    ] = pydantic.Field(alias="apple_pay_later", default=None)
    au_becs_debit: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAuBecsDebit
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    bancontact: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBancontact
    ] = pydantic.Field(alias="bancontact", default=None)
    billie: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyBillie] = (
        pydantic.Field(alias="billie", default=None)
    )
    blik: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyBlik] = (
        pydantic.Field(alias="blik", default=None)
    )
    boleto: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyBoleto] = (
        pydantic.Field(alias="boleto", default=None)
    )
    card: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyCard] = (
        pydantic.Field(alias="card", default=None)
    )
    cartes_bancaires: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyCartesBancaires
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
    cashapp: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyCashapp] = (
        pydantic.Field(alias="cashapp", default=None)
    )
    customer_balance: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyCustomerBalance
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyEps] = (
        pydantic.Field(alias="eps", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fpx: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyFpx] = (
        pydantic.Field(alias="fpx", default=None)
    )
    giropay: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyGiropay] = (
        pydantic.Field(alias="giropay", default=None)
    )
    google_pay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyGooglePay
    ] = pydantic.Field(alias="google_pay", default=None)
    grabpay: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyGrabpay] = (
        pydantic.Field(alias="grabpay", default=None)
    )
    ideal: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyIdeal] = (
        pydantic.Field(alias="ideal", default=None)
    )
    jcb: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyJcb] = (
        pydantic.Field(alias="jcb", default=None)
    )
    klarna: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyKlarna] = (
        pydantic.Field(alias="klarna", default=None)
    )
    konbini: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyKonbini] = (
        pydantic.Field(alias="konbini", default=None)
    )
    link: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyLink] = (
        pydantic.Field(alias="link", default=None)
    )
    mobilepay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyMobilepay
    ] = pydantic.Field(alias="mobilepay", default=None)
    multibanco: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyMultibanco
    ] = pydantic.Field(alias="multibanco", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    nz_bank_account: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyNzBankAccount
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    oxxo: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyOxxo] = (
        pydantic.Field(alias="oxxo", default=None)
    )
    p24: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyP24] = (
        pydantic.Field(alias="p24", default=None)
    )
    pay_by_bank: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyPayByBank
    ] = pydantic.Field(alias="pay_by_bank", default=None)
    paynow: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyPaynow] = (
        pydantic.Field(alias="paynow", default=None)
    )
    paypal: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyPaypal] = (
        pydantic.Field(alias="paypal", default=None)
    )
    promptpay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyPromptpay
    ] = pydantic.Field(alias="promptpay", default=None)
    revolut_pay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyRevolutPay
    ] = pydantic.Field(alias="revolut_pay", default=None)
    satispay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodySatispay
    ] = pydantic.Field(alias="satispay", default=None)
    sepa_debit: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodySepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    sofort: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodySofort] = (
        pydantic.Field(alias="sofort", default=None)
    )
    swish: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodySwish] = (
        pydantic.Field(alias="swish", default=None)
    )
    twint: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyTwint] = (
        pydantic.Field(alias="twint", default=None)
    )
    us_bank_account: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyWechatPay
    ] = pydantic.Field(alias="wechat_pay", default=None)
    zip: typing.Optional[_SerializerPaymentMethodConfigurationUpdateBodyZip] = (
        pydantic.Field(alias="zip", default=None)
    )
