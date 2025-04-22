import pydantic
import typing
import typing_extensions

from .source_code_verification_flow import SourceCodeVerificationFlow
from .source_metadata import SourceMetadata
from .source_order import SourceOrder
from .source_owner import SourceOwner
from .source_receiver_flow import SourceReceiverFlow
from .source_redirect_flow import SourceRedirectFlow
from .source_type_ach_credit_transfer import SourceTypeAchCreditTransfer
from .source_type_ach_debit import SourceTypeAchDebit
from .source_type_acss_debit import SourceTypeAcssDebit
from .source_type_alipay import SourceTypeAlipay
from .source_type_au_becs_debit import SourceTypeAuBecsDebit
from .source_type_bancontact import SourceTypeBancontact
from .source_type_card import SourceTypeCard
from .source_type_card_present import SourceTypeCardPresent
from .source_type_eps import SourceTypeEps
from .source_type_giropay import SourceTypeGiropay
from .source_type_ideal import SourceTypeIdeal
from .source_type_klarna import SourceTypeKlarna
from .source_type_multibanco import SourceTypeMultibanco
from .source_type_p24 import SourceTypeP24
from .source_type_sepa_debit import SourceTypeSepaDebit
from .source_type_sofort import SourceTypeSofort
from .source_type_three_d_secure import SourceTypeThreeDSecure
from .source_type_wechat import SourceTypeWechat


class Source(pydantic.BaseModel):
    """
    `Source` objects allow you to accept a variety of payment methods. They
    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
    This newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach_credit_transfer: typing.Optional[SourceTypeAchCreditTransfer] = pydantic.Field(
        alias="ach_credit_transfer", default=None
    )
    ach_debit: typing.Optional[SourceTypeAchDebit] = pydantic.Field(
        alias="ach_debit", default=None
    )
    acss_debit: typing.Optional[SourceTypeAcssDebit] = pydantic.Field(
        alias="acss_debit", default=None
    )
    alipay: typing.Optional[SourceTypeAlipay] = pydantic.Field(
        alias="alipay", default=None
    )
    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
    """
    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.
    """
    au_becs_debit: typing.Optional[SourceTypeAuBecsDebit] = pydantic.Field(
        alias="au_becs_debit", default=None
    )
    bancontact: typing.Optional[SourceTypeBancontact] = pydantic.Field(
        alias="bancontact", default=None
    )
    card: typing.Optional[SourceTypeCard] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[SourceTypeCardPresent] = pydantic.Field(
        alias="card_present", default=None
    )
    client_secret: str = pydantic.Field(
        alias="client_secret",
    )
    """
    The client secret of the source. Used for client-side retrieval using a publishable key.
    """
    code_verification: typing.Optional[SourceCodeVerificationFlow] = pydantic.Field(
        alias="code_verification", default=None
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources.
    """
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    """
    The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.
    """
    eps: typing.Optional[SourceTypeEps] = pydantic.Field(alias="eps", default=None)
    flow: str = pydantic.Field(
        alias="flow",
    )
    """
    The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.
    """
    giropay: typing.Optional[SourceTypeGiropay] = pydantic.Field(
        alias="giropay", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    ideal: typing.Optional[SourceTypeIdeal] = pydantic.Field(
        alias="ideal", default=None
    )
    klarna: typing.Optional[SourceTypeKlarna] = pydantic.Field(
        alias="klarna", default=None
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[SourceMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    multibanco: typing.Optional[SourceTypeMultibanco] = pydantic.Field(
        alias="multibanco", default=None
    )
    object: typing_extensions.Literal["source"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    owner: typing.Optional[SourceOwner] = pydantic.Field(alias="owner", default=None)
    p24: typing.Optional[SourceTypeP24] = pydantic.Field(alias="p24", default=None)
    receiver: typing.Optional[SourceReceiverFlow] = pydantic.Field(
        alias="receiver", default=None
    )
    redirect: typing.Optional[SourceRedirectFlow] = pydantic.Field(
        alias="redirect", default=None
    )
    sepa_debit: typing.Optional[SourceTypeSepaDebit] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    sofort: typing.Optional[SourceTypeSofort] = pydantic.Field(
        alias="sofort", default=None
    )
    source_order: typing.Optional[SourceOrder] = pydantic.Field(
        alias="source_order", default=None
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    Extra information about a source. This will appear on your customer's statement every time you charge the source.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge.
    """
    three_d_secure: typing.Optional[SourceTypeThreeDSecure] = pydantic.Field(
        alias="three_d_secure", default=None
    )
    type_: typing_extensions.Literal[
        "ach_credit_transfer",
        "ach_debit",
        "acss_debit",
        "alipay",
        "au_becs_debit",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://stripe.com/docs/sources) used.
    """
    usage: typing.Optional[str] = pydantic.Field(alias="usage", default=None)
    """
    Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned.
    """
    wechat: typing.Optional[SourceTypeWechat] = pydantic.Field(
        alias="wechat", default=None
    )
