import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyFuel(typing_extensions.TypedDict):
    """
    Information about fuel that was purchased with this transaction.
    """

    industry_product_code: typing_extensions.NotRequired[str]

    quantity_decimal: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "diesel", "other", "unleaded_plus", "unleaded_regular", "unleaded_super"
        ]
    ]

    unit: typing_extensions.NotRequired[
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
    ]

    unit_cost_decimal: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCreateBodyFuel(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyFuel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    industry_product_code: typing.Optional[str] = pydantic.Field(
        alias="industry_product_code", default=None
    )
    quantity_decimal: typing.Optional[str] = pydantic.Field(
        alias="quantity_decimal", default=None
    )
    type_: typing.Optional[
        typing_extensions.Literal[
            "diesel", "other", "unleaded_plus", "unleaded_regular", "unleaded_super"
        ]
    ] = pydantic.Field(alias="type", default=None)
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
    unit_cost_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_cost_decimal", default=None
    )
