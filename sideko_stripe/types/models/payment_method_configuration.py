import pydantic
import typing
import typing_extensions

from .payment_method_config_resource_payment_method_properties import (
    PaymentMethodConfigResourcePaymentMethodProperties,
)


class PaymentMethodConfiguration(pydantic.BaseModel):
    """
    PaymentMethodConfigurations control which payment methods are displayed to your customers when you don't explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

    There are two types of PaymentMethodConfigurations. Which is used depends on the [charge type](https://stripe.com/docs/connect/charges):

    **Direct** configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

    **Child** configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

    Child configurations have a `parent` that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are [managed in the dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts) and are not available in this API.

    Related guides:
    - [Payment Method Configurations API](https://stripe.com/docs/connect/payment-method-configurations)
    - [Multiple configurations on dynamic payment methods](https://stripe.com/docs/payments/multiple-payment-method-configs)
    - [Multiple configurations for your Connect accounts](https://stripe.com/docs/connect/multiple-payment-method-configurations)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="acss_debit", default=None)
    )
    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the configuration can be used for new payments.
    """
    affirm: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="affirm", default=None)
    )
    afterpay_clearpay: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="afterpay_clearpay", default=None)
    alipay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="alipay", default=None)
    )
    alma: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="alma", default=None)
    )
    amazon_pay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="amazon_pay", default=None)
    )
    apple_pay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="apple_pay", default=None)
    )
    application: typing.Optional[str] = pydantic.Field(
        alias="application", default=None
    )
    """
    For child configs, the Connect application associated with the configuration.
    """
    au_becs_debit: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="au_becs_debit", default=None)
    bacs_debit: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="bacs_debit", default=None)
    )
    bancontact: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="bancontact", default=None)
    )
    billie: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="billie", default=None)
    )
    blik: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="blik", default=None)
    )
    boleto: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="boleto", default=None)
    )
    card: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="card", default=None)
    )
    cartes_bancaires: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="cartes_bancaires", default=None)
    cashapp: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="cashapp", default=None)
    )
    customer_balance: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="customer_balance", default=None)
    eps: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="eps", default=None)
    )
    fpx: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="fpx", default=None)
    )
    giropay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="giropay", default=None)
    )
    google_pay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="google_pay", default=None)
    )
    grabpay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="grabpay", default=None)
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    ideal: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="ideal", default=None)
    )
    is_default: bool = pydantic.Field(
        alias="is_default",
    )
    """
    The default configuration is used whenever a payment method configuration is not specified.
    """
    jcb: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="jcb", default=None)
    )
    klarna: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="klarna", default=None)
    )
    konbini: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="konbini", default=None)
    )
    link: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="link", default=None)
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    mobilepay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="mobilepay", default=None)
    )
    multibanco: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="multibanco", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The configuration's name.
    """
    nz_bank_account: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="nz_bank_account", default=None)
    object: typing_extensions.Literal["payment_method_configuration"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    oxxo: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="oxxo", default=None)
    )
    p24: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="p24", default=None)
    )
    parent: typing.Optional[str] = pydantic.Field(alias="parent", default=None)
    """
    For child configs, the configuration's parent configuration.
    """
    pay_by_bank: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="pay_by_bank", default=None)
    )
    paynow: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="paynow", default=None)
    )
    paypal: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="paypal", default=None)
    )
    promptpay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="promptpay", default=None)
    )
    revolut_pay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="revolut_pay", default=None)
    )
    satispay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="satispay", default=None)
    )
    sepa_debit: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="sepa_debit", default=None)
    )
    sofort: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="sofort", default=None)
    )
    swish: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="swish", default=None)
    )
    twint: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="twint", default=None)
    )
    us_bank_account: typing.Optional[
        PaymentMethodConfigResourcePaymentMethodProperties
    ] = pydantic.Field(alias="us_bank_account", default=None)
    wechat_pay: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="wechat_pay", default=None)
    )
    zip: typing.Optional[PaymentMethodConfigResourcePaymentMethodProperties] = (
        pydantic.Field(alias="zip", default=None)
    )
