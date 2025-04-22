import pydantic
import typing
import typing_extensions


class TaxCalculationCreateBodyShippingCost(typing_extensions.TypedDict):
    """
    Shipping cost details to be used for the calculation.
    """

    amount: typing_extensions.NotRequired[int]

    shipping_rate: typing_extensions.NotRequired[str]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive"]
    ]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerTaxCalculationCreateBodyShippingCost(pydantic.BaseModel):
    """
    Serializer for TaxCalculationCreateBodyShippingCost handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
