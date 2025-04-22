import pydantic
import typing
import typing_extensions

from .coupon_create_body_applies_to import (
    CouponCreateBodyAppliesTo,
    _SerializerCouponCreateBodyAppliesTo,
)
from .coupon_create_body_currency_options import (
    CouponCreateBodyCurrencyOptions,
    _SerializerCouponCreateBodyCurrencyOptions,
)
from .coupon_create_body_metadata_obj0 import (
    CouponCreateBodyMetadataObj0,
    _SerializerCouponCreateBodyMetadataObj0,
)


class CouponCreateBody(typing_extensions.TypedDict, total=False):
    """
    CouponCreateBody
    """

    amount_off: typing_extensions.NotRequired[int]
    """
    A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed).
    """

    applies_to: typing_extensions.NotRequired[CouponCreateBodyAppliesTo]
    """
    A hash containing directions for what this Coupon will apply discounts to.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).
    """

    currency_options: typing_extensions.NotRequired[CouponCreateBodyCurrencyOptions]
    """
    Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    duration: typing_extensions.NotRequired[
        typing_extensions.Literal["forever", "once", "repeating"]
    ]
    """
    Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`.
    """

    duration_in_months: typing_extensions.NotRequired[int]
    """
    Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    id: typing_extensions.NotRequired[str]
    """
    Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you.
    """

    max_redemptions: typing_extensions.NotRequired[int]
    """
    A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CouponCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
    """

    percent_off: typing_extensions.NotRequired[float]
    """
    A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).
    """

    redeem_by: typing_extensions.NotRequired[int]
    """
    Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers.
    """


class _SerializerCouponCreateBody(pydantic.BaseModel):
    """
    Serializer for CouponCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount_off: typing.Optional[int] = pydantic.Field(alias="amount_off", default=None)
    applies_to: typing.Optional[_SerializerCouponCreateBodyAppliesTo] = pydantic.Field(
        alias="applies_to", default=None
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    currency_options: typing.Optional[_SerializerCouponCreateBodyCurrencyOptions] = (
        pydantic.Field(alias="currency_options", default=None)
    )
    duration: typing.Optional[
        typing_extensions.Literal["forever", "once", "repeating"]
    ] = pydantic.Field(alias="duration", default=None)
    duration_in_months: typing.Optional[int] = pydantic.Field(
        alias="duration_in_months", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    max_redemptions: typing.Optional[int] = pydantic.Field(
        alias="max_redemptions", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCouponCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    percent_off: typing.Optional[float] = pydantic.Field(
        alias="percent_off", default=None
    )
    redeem_by: typing.Optional[int] = pydantic.Field(alias="redeem_by", default=None)
