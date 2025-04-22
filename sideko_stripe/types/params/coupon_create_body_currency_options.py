import pydantic
import typing
import typing_extensions

from .coupon_create_body_currency_options_additional_props import (
    CouponCreateBodyCurrencyOptionsAdditionalProps,
    _SerializerCouponCreateBodyCurrencyOptionsAdditionalProps,
)


class CouponCreateBodyCurrencyOptions(typing_extensions.TypedDict, total=False):
    """
    Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """


class _SerializerCouponCreateBodyCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for CouponCreateBodyCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerCouponCreateBodyCurrencyOptionsAdditionalProps
    ]
