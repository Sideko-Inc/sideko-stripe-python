import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_create_body_amount_details import (
    TestHelperIssuingAuthorizationCreateBodyAmountDetails,
    _SerializerTestHelperIssuingAuthorizationCreateBodyAmountDetails,
)
from .test_helper_issuing_authorization_create_body_fleet import (
    TestHelperIssuingAuthorizationCreateBodyFleet,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleet,
)
from .test_helper_issuing_authorization_create_body_fuel import (
    TestHelperIssuingAuthorizationCreateBodyFuel,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFuel,
)
from .test_helper_issuing_authorization_create_body_merchant_data import (
    TestHelperIssuingAuthorizationCreateBodyMerchantData,
    _SerializerTestHelperIssuingAuthorizationCreateBodyMerchantData,
)
from .test_helper_issuing_authorization_create_body_network_data import (
    TestHelperIssuingAuthorizationCreateBodyNetworkData,
    _SerializerTestHelperIssuingAuthorizationCreateBodyNetworkData,
)
from .test_helper_issuing_authorization_create_body_verification_data import (
    TestHelperIssuingAuthorizationCreateBodyVerificationData,
    _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationData,
)


class TestHelperIssuingAuthorizationCreateBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    amount_details: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyAmountDetails
    ]
    """
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    authorization_method: typing_extensions.NotRequired[
        typing_extensions.Literal["chip", "contactless", "keyed_in", "online", "swipe"]
    ]
    """
    How the card details were provided. Defaults to online.
    """

    card: typing_extensions.Required[str]
    """
    Card associated with this authorization.
    """

    currency: typing_extensions.NotRequired[str]
    """
    The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fleet: typing_extensions.NotRequired[TestHelperIssuingAuthorizationCreateBodyFleet]
    """
    Fleet-specific information for authorizations using Fleet cards.
    """

    fuel: typing_extensions.NotRequired[TestHelperIssuingAuthorizationCreateBodyFuel]
    """
    Information about fuel that was purchased with this transaction.
    """

    is_amount_controllable: typing_extensions.NotRequired[bool]
    """
    If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
    """

    merchant_amount: typing_extensions.NotRequired[int]
    """
    The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    merchant_currency: typing_extensions.NotRequired[str]
    """
    The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    merchant_data: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyMerchantData
    ]
    """
    Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    """

    network_data: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyNetworkData
    ]
    """
    Details about the authorization, such as identifiers, set by the card network.
    """

    verification_data: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyVerificationData
    ]
    """
    Verifications that Stripe performed on information that the cardholder provided to the merchant.
    """

    wallet: typing_extensions.NotRequired[
        typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
    ]
    """
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.
    """


class _SerializerTestHelperIssuingAuthorizationCreateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    amount_details: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyAmountDetails
    ] = pydantic.Field(alias="amount_details", default=None)
    authorization_method: typing.Optional[
        typing_extensions.Literal["chip", "contactless", "keyed_in", "online", "swipe"]
    ] = pydantic.Field(alias="authorization_method", default=None)
    card: str = pydantic.Field(
        alias="card",
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fleet: typing.Optional[_SerializerTestHelperIssuingAuthorizationCreateBodyFleet] = (
        pydantic.Field(alias="fleet", default=None)
    )
    fuel: typing.Optional[_SerializerTestHelperIssuingAuthorizationCreateBodyFuel] = (
        pydantic.Field(alias="fuel", default=None)
    )
    is_amount_controllable: typing.Optional[bool] = pydantic.Field(
        alias="is_amount_controllable", default=None
    )
    merchant_amount: typing.Optional[int] = pydantic.Field(
        alias="merchant_amount", default=None
    )
    merchant_currency: typing.Optional[str] = pydantic.Field(
        alias="merchant_currency", default=None
    )
    merchant_data: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyMerchantData
    ] = pydantic.Field(alias="merchant_data", default=None)
    network_data: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyNetworkData
    ] = pydantic.Field(alias="network_data", default=None)
    verification_data: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationData
    ] = pydantic.Field(alias="verification_data", default=None)
    wallet: typing.Optional[
        typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
    ] = pydantic.Field(alias="wallet", default=None)
