import pydantic
import typing
import typing_extensions

from .charge_create_body_card_obj0 import (
    ChargeCreateBodyCardObj0,
    _SerializerChargeCreateBodyCardObj0,
)
from .charge_create_body_destination_obj0 import (
    ChargeCreateBodyDestinationObj0,
    _SerializerChargeCreateBodyDestinationObj0,
)
from .charge_create_body_metadata_obj0 import (
    ChargeCreateBodyMetadataObj0,
    _SerializerChargeCreateBodyMetadataObj0,
)
from .charge_create_body_radar_options import (
    ChargeCreateBodyRadarOptions,
    _SerializerChargeCreateBodyRadarOptions,
)
from .charge_create_body_shipping import (
    ChargeCreateBodyShipping,
    _SerializerChargeCreateBodyShipping,
)
from .charge_create_body_transfer_data import (
    ChargeCreateBodyTransferData,
    _SerializerChargeCreateBodyTransferData,
)


class ChargeCreateBody(typing_extensions.TypedDict, total=False):
    """
    ChargeCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """

    application_fee: typing_extensions.NotRequired[int]

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collect-fees).
    """

    capture: typing_extensions.NotRequired[bool]
    """
    Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation.
    """

    card: typing_extensions.NotRequired[typing.Union[ChargeCreateBodyCardObj0, str]]
    """
    A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.NotRequired[str]
    """
    The ID of an existing customer that will be charged in this request.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
    """

    destination: typing_extensions.NotRequired[
        typing.Union[ChargeCreateBodyDestinationObj0, str]
    ]

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ChargeCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant).
    """

    radar_options: typing_extensions.NotRequired[ChargeCreateBodyRadarOptions]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """

    receipt_email: typing_extensions.NotRequired[str]
    """
    The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    """

    shipping: typing_extensions.NotRequired[ChargeCreateBodyShipping]
    """
    Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    """

    source: typing_extensions.NotRequired[str]
    """
    A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    
    For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    """

    statement_descriptor_suffix: typing_extensions.NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    """

    transfer_data: typing_extensions.NotRequired[ChargeCreateBodyTransferData]
    """
    An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options).
    """


class _SerializerChargeCreateBody(pydantic.BaseModel):
    """
    Serializer for ChargeCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    application_fee: typing.Optional[int] = pydantic.Field(
        alias="application_fee", default=None
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    capture: typing.Optional[bool] = pydantic.Field(alias="capture", default=None)
    card: typing.Optional[typing.Union[_SerializerChargeCreateBodyCardObj0, str]] = (
        pydantic.Field(alias="card", default=None)
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    destination: typing.Optional[
        typing.Union[_SerializerChargeCreateBodyDestinationObj0, str]
    ] = pydantic.Field(alias="destination", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerChargeCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    radar_options: typing.Optional[_SerializerChargeCreateBodyRadarOptions] = (
        pydantic.Field(alias="radar_options", default=None)
    )
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    shipping: typing.Optional[_SerializerChargeCreateBodyShipping] = pydantic.Field(
        alias="shipping", default=None
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[_SerializerChargeCreateBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
