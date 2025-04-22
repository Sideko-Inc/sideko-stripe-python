import pydantic
import typing
import typing_extensions

from .product_create_body_default_price_data_currency_options import (
    ProductCreateBodyDefaultPriceDataCurrencyOptions,
    _SerializerProductCreateBodyDefaultPriceDataCurrencyOptions,
)
from .product_create_body_default_price_data_custom_unit_amount import (
    ProductCreateBodyDefaultPriceDataCustomUnitAmount,
    _SerializerProductCreateBodyDefaultPriceDataCustomUnitAmount,
)
from .product_create_body_default_price_data_metadata import (
    ProductCreateBodyDefaultPriceDataMetadata,
    _SerializerProductCreateBodyDefaultPriceDataMetadata,
)
from .product_create_body_default_price_data_recurring import (
    ProductCreateBodyDefaultPriceDataRecurring,
    _SerializerProductCreateBodyDefaultPriceDataRecurring,
)


class ProductCreateBodyDefaultPriceData(typing_extensions.TypedDict):
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product.
    """

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        ProductCreateBodyDefaultPriceDataCurrencyOptions
    ]

    custom_unit_amount: typing_extensions.NotRequired[
        ProductCreateBodyDefaultPriceDataCustomUnitAmount
    ]

    metadata: typing_extensions.NotRequired[ProductCreateBodyDefaultPriceDataMetadata]

    recurring: typing_extensions.NotRequired[ProductCreateBodyDefaultPriceDataRecurring]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerProductCreateBodyDefaultPriceData(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyDefaultPriceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    currency_options: typing.Optional[
        _SerializerProductCreateBodyDefaultPriceDataCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
    custom_unit_amount: typing.Optional[
        _SerializerProductCreateBodyDefaultPriceDataCustomUnitAmount
    ] = pydantic.Field(alias="custom_unit_amount", default=None)
    metadata: typing.Optional[_SerializerProductCreateBodyDefaultPriceDataMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    recurring: typing.Optional[
        _SerializerProductCreateBodyDefaultPriceDataRecurring
    ] = pydantic.Field(alias="recurring", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
