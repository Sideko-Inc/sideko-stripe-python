import pydantic
import typing


class TaxProductResourceTaxTransactionResourceReversal(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    original_transaction: typing.Optional[str] = pydantic.Field(
        alias="original_transaction", default=None
    )
    """
    The `id` of the reversed `Transaction` object.
    """
