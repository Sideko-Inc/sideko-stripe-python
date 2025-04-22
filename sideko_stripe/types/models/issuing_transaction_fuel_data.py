import pydantic
import typing


class IssuingTransactionFuelData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    industry_product_code: typing.Optional[str] = pydantic.Field(
        alias="industry_product_code", default=None
    )
    """
    [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.
    """
    quantity_decimal: typing.Optional[str] = pydantic.Field(
        alias="quantity_decimal", default=None
    )
    """
    The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.
    """
    unit: str = pydantic.Field(
        alias="unit",
    )
    """
    The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.
    """
    unit_cost_decimal: str = pydantic.Field(
        alias="unit_cost_decimal",
    )
    """
    The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.
    """
