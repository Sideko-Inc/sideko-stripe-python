import pydantic
import typing
import typing_extensions

from .coupon_update_body_currency_options import (
    CouponUpdateBodyCurrencyOptions,
    _SerializerCouponUpdateBodyCurrencyOptions,
)
from .coupon_update_body_metadata_obj0 import (
    CouponUpdateBodyMetadataObj0,
    _SerializerCouponUpdateBodyMetadataObj0,
)


class CouponUpdateBody(typing_extensions.TypedDict, total=False):
    """
    CouponUpdateBody
    """

    currency_options: typing_extensions.NotRequired[CouponUpdateBodyCurrencyOptions]
    """
    Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CouponUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
    """


class _SerializerCouponUpdateBody(pydantic.BaseModel):
    """
    Serializer for CouponUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    currency_options: typing.Optional[_SerializerCouponUpdateBodyCurrencyOptions] = (
        pydantic.Field(alias="currency_options", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCouponUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
