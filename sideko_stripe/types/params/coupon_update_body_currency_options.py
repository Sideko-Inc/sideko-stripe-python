import pydantic
import typing
import typing_extensions

from .coupon_update_body_currency_options_additional_props import (
    CouponUpdateBodyCurrencyOptionsAdditionalProps,
    _SerializerCouponUpdateBodyCurrencyOptionsAdditionalProps,
)


class CouponUpdateBodyCurrencyOptions(typing_extensions.TypedDict, total=False):
    """
    Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """


class _SerializerCouponUpdateBodyCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for CouponUpdateBodyCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerCouponUpdateBodyCurrencyOptionsAdditionalProps
    ]
