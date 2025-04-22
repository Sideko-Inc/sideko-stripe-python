import pydantic
import typing
import typing_extensions


class IssuingAuthorizationFuelData(pydantic.BaseModel):
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
    type_: typing.Optional[
        typing_extensions.Literal[
            "diesel", "other", "unleaded_plus", "unleaded_regular", "unleaded_super"
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    The type of fuel that was purchased.
    """
    unit: typing.Optional[
        typing_extensions.Literal[
            "charging_minute",
            "imperial_gallon",
            "kilogram",
            "kilowatt_hour",
            "liter",
            "other",
            "pound",
            "us_gallon",
        ]
    ] = pydantic.Field(alias="unit", default=None)
    """
    The units for `quantity_decimal`.
    """
    unit_cost_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_cost_decimal", default=None
    )
    """
    The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.
    """
