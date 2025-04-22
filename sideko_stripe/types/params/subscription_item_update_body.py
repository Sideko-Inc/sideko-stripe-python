import pydantic
import typing
import typing_extensions

from .subscription_item_update_body_discounts_arr0_item import (
    SubscriptionItemUpdateBodyDiscountsArr0Item,
    _SerializerSubscriptionItemUpdateBodyDiscountsArr0Item,
)
from .subscription_item_update_body_metadata_obj0 import (
    SubscriptionItemUpdateBodyMetadataObj0,
    _SerializerSubscriptionItemUpdateBodyMetadataObj0,
)
from .subscription_item_update_body_price_data import (
    SubscriptionItemUpdateBodyPriceData,
    _SerializerSubscriptionItemUpdateBodyPriceData,
)


class SubscriptionItemUpdateBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionItemUpdateBody
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[SubscriptionItemUpdateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons to redeem into discounts for the subscription item.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[SubscriptionItemUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    off_session: typing_extensions.NotRequired[bool]
    """
    Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    """

    payment_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ]
    """
    Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.
    
    Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.
    
    Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).
    
    Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    """

    price: typing_extensions.NotRequired[str]
    """
    The ID of the price object. One of `price` or `price_data` is required. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
    """

    price_data: typing_extensions.NotRequired[SubscriptionItemUpdateBodyPriceData]
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """

    proration_date: typing_extensions.NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
    """

    quantity: typing_extensions.NotRequired[int]
    """
    The quantity you'd like to apply to the subscription item you're creating.
    """

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]
    """
    A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
    """


class _SerializerSubscriptionItemUpdateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionItemUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerSubscriptionItemUpdateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerSubscriptionItemUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    off_session: typing.Optional[bool] = pydantic.Field(
        alias="off_session", default=None
    )
    payment_behavior: typing.Optional[
        typing_extensions.Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ] = pydantic.Field(alias="payment_behavior", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[_SerializerSubscriptionItemUpdateBodyPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    proration_date: typing.Optional[int] = pydantic.Field(
        alias="proration_date", default=None
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
