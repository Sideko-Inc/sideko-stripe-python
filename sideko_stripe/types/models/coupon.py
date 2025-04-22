import pydantic
import typing
import typing_extensions

from .coupon_applies_to import CouponAppliesTo
from .coupon_currency_options import CouponCurrencyOptions
from .coupon_metadata import CouponMetadata


class Coupon(pydantic.BaseModel):
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_off: typing.Optional[int] = pydantic.Field(alias="amount_off", default=None)
    """
    Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.
    """
    applies_to: typing.Optional[CouponAppliesTo] = pydantic.Field(
        alias="applies_to", default=None
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.
    """
    currency_options: typing.Optional[CouponCurrencyOptions] = pydantic.Field(
        alias="currency_options", default=None
    )
    """
    Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """
    duration: typing_extensions.Literal["forever", "once", "repeating"] = (
        pydantic.Field(
            alias="duration",
        )
    )
    """
    One of `forever`, `once`, and `repeating`. Describes how long a customer who applies this coupon will get the discount.
    """
    duration_in_months: typing.Optional[int] = pydantic.Field(
        alias="duration_in_months", default=None
    )
    """
    If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    max_redemptions: typing.Optional[int] = pydantic.Field(
        alias="max_redemptions", default=None
    )
    """
    Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.
    """
    metadata: typing.Optional[CouponMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of the coupon displayed to customers on for instance invoices or receipts.
    """
    object: typing_extensions.Literal["coupon"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percent_off: typing.Optional[float] = pydantic.Field(
        alias="percent_off", default=None
    )
    """
    Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $ (or local equivalent)100 invoice $ (or local equivalent)50 instead.
    """
    redeem_by: typing.Optional[int] = pydantic.Field(alias="redeem_by", default=None)
    """
    Date after which the coupon can no longer be redeemed.
    """
    times_redeemed: int = pydantic.Field(
        alias="times_redeemed",
    )
    """
    Number of times this coupon has been applied to a customer.
    """
    valid: bool = pydantic.Field(
        alias="valid",
    )
    """
    Taking account of the above properties, whether this coupon can still be applied to a customer.
    """
