import pydantic
import typing
import typing_extensions

from .coupon import Coupon
from .deleted_customer import DeletedCustomer
from .promotion_code_metadata import PromotionCodeMetadata
from .promotion_codes_resource_restrictions import PromotionCodesResourceRestrictions

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer


class PromotionCode(pydantic.BaseModel):
    """
    A Promotion Code represents a customer-redeemable code for a [coupon](https://stripe.com/docs/api#coupons). It can be used to
    create multiple codes for a single coupon.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid.
    """
    code: str = pydantic.Field(
        alias="code",
    )
    """
    The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).
    """
    coupon: Coupon = pydantic.Field(
        alias="coupon",
    )
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The customer that this promotion code can be used by.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    Date at which the promotion code can no longer be redeemed.
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
    Maximum number of times this promotion code can be redeemed.
    """
    metadata: typing.Optional[PromotionCodeMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["promotion_code"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    restrictions: PromotionCodesResourceRestrictions = pydantic.Field(
        alias="restrictions",
    )
    times_redeemed: int = pydantic.Field(
        alias="times_redeemed",
    )
    """
    Number of times this promotion code has been used.
    """
