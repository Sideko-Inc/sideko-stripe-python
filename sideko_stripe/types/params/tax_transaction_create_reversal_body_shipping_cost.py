import pydantic
import typing_extensions


class TaxTransactionCreateReversalBodyShippingCost(typing_extensions.TypedDict):
    """
    The shipping cost to reverse.
    """

    amount: typing_extensions.Required[int]

    amount_tax: typing_extensions.Required[int]


class _SerializerTaxTransactionCreateReversalBodyShippingCost(pydantic.BaseModel):
    """
    Serializer for TaxTransactionCreateReversalBodyShippingCost handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
