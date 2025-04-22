import pydantic
import typing
import typing_extensions


class TaxCalculationCreateBodyLineItemsItem(typing_extensions.TypedDict):
    """
    TaxCalculationCreateBodyLineItemsItem
    """

    amount: typing_extensions.Required[int]

    product: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[int]

    reference: typing_extensions.NotRequired[str]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive"]
    ]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerTaxCalculationCreateBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for TaxCalculationCreateBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
