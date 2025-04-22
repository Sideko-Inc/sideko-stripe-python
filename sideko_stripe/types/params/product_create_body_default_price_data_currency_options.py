import pydantic
import typing
import typing_extensions

from .product_create_body_default_price_data_currency_options_additional_props import (
    ProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps,
    _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps,
)


class ProductCreateBodyDefaultPriceDataCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    ProductCreateBodyDefaultPriceDataCurrencyOptions
    """


class _SerializerProductCreateBodyDefaultPriceDataCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyDefaultPriceDataCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerProductCreateBodyDefaultPriceDataCurrencyOptionsAdditionalProps
    ]
