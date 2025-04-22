import pydantic
import typing
import typing_extensions

from .product_create_body_default_price_data_currency_options_additional_props_custom_unit_amount import (
    ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsCustomUnitAmount,
    _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsCustomUnitAmount,
)
from .product_create_body_default_price_data_currency_options_additional_props_tiers_item import (
    ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsTiersItem,
    _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsTiersItem,
)


class ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps
    """

    custom_unit_amount: typing_extensions.NotRequired[
        ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsCustomUnitAmount
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tiers: typing_extensions.NotRequired[
        typing.List[
            ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsTiersItem
        ]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_unit_amount: typing.Optional[
        _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsCustomUnitAmount
    ] = pydantic.Field(alias="custom_unit_amount", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tiers: typing.Optional[
        typing.List[
            _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalPropsTiersItem
        ]
    ] = pydantic.Field(alias="tiers", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
