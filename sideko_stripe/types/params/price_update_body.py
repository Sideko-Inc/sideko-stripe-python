import pydantic
import typing
import typing_extensions

from .price_update_body_currency_options_obj0 import (
    PriceUpdateBodyCurrencyOptionsObj0,
    _SerializerPriceUpdateBodyCurrencyOptionsObj0,
)
from .price_update_body_metadata_obj0 import (
    PriceUpdateBodyMetadataObj0,
    _SerializerPriceUpdateBodyMetadataObj0,
)


class PriceUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PriceUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the price can be used for new purchases. Defaults to `true`.
    """

    currency_options: typing_extensions.NotRequired[
        typing.Union[PriceUpdateBodyCurrencyOptionsObj0, str]
    ]
    """
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    lookup_key: typing_extensions.NotRequired[str]
    """
    A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PriceUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nickname: typing_extensions.NotRequired[str]
    """
    A brief description of the price, hidden from customers.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """

    transfer_lookup_key: typing_extensions.NotRequired[bool]
    """
    If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.
    """


class _SerializerPriceUpdateBody(pydantic.BaseModel):
    """
    Serializer for PriceUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    currency_options: typing.Optional[
        typing.Union[_SerializerPriceUpdateBodyCurrencyOptionsObj0, str]
    ] = pydantic.Field(alias="currency_options", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    lookup_key: typing.Optional[str] = pydantic.Field(alias="lookup_key", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerPriceUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    transfer_lookup_key: typing.Optional[bool] = pydantic.Field(
        alias="transfer_lookup_key", default=None
    )
