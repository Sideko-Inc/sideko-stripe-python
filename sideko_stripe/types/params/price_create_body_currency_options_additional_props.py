import pydantic
import typing
import typing_extensions

from .price_create_body_currency_options_additional_props_custom_unit_amount import (
    PriceCreateBodyCurrencyOptionsAdditionalPropsCustomUnitAmount,
    _SerializerPriceCreateBodyCurrencyOptionsAdditionalPropsCustomUnitAmount,
)
from .price_create_body_currency_options_additional_props_tiers_item import (
    PriceCreateBodyCurrencyOptionsAdditionalPropsTiersItem,
    _SerializerPriceCreateBodyCurrencyOptionsAdditionalPropsTiersItem,
)


class PriceCreateBodyCurrencyOptionsAdditionalProps(typing_extensions.TypedDict):
    """
    PriceCreateBodyCurrencyOptionsAdditionalProps
    """

    custom_unit_amount: typing_extensions.NotRequired[
        PriceCreateBodyCurrencyOptionsAdditionalPropsCustomUnitAmount
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tiers: typing_extensions.NotRequired[
        typing.List[PriceCreateBodyCurrencyOptionsAdditionalPropsTiersItem]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerPriceCreateBodyCurrencyOptionsAdditionalProps(pydantic.BaseModel):
    """
    Serializer for PriceCreateBodyCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_unit_amount: typing.Optional[
        _SerializerPriceCreateBodyCurrencyOptionsAdditionalPropsCustomUnitAmount
    ] = pydantic.Field(alias="custom_unit_amount", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tiers: typing.Optional[
        typing.List[_SerializerPriceCreateBodyCurrencyOptionsAdditionalPropsTiersItem]
    ] = pydantic.Field(alias="tiers", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
