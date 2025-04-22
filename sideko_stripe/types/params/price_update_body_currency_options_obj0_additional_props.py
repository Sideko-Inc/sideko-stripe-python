import pydantic
import typing
import typing_extensions

from .price_update_body_currency_options_obj0_additional_props_custom_unit_amount import (
    PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount,
    _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount,
)
from .price_update_body_currency_options_obj0_additional_props_tiers_item import (
    PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem,
    _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem,
)


class PriceUpdateBodyCurrencyOptionsObj0AdditionalProps(typing_extensions.TypedDict):
    """
    PriceUpdateBodyCurrencyOptionsObj0AdditionalProps
    """

    custom_unit_amount: typing_extensions.NotRequired[
        PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tiers: typing_extensions.NotRequired[
        typing.List[PriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalProps(pydantic.BaseModel):
    """
    Serializer for PriceUpdateBodyCurrencyOptionsObj0AdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_unit_amount: typing.Optional[
        _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsCustomUnitAmount
    ] = pydantic.Field(alias="custom_unit_amount", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tiers: typing.Optional[
        typing.List[
            _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalPropsTiersItem
        ]
    ] = pydantic.Field(alias="tiers", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
