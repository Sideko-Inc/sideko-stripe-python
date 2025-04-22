import pydantic
import typing
import typing_extensions


class TaxTransactionCreateReversalBodyLineItemsItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    TaxTransactionCreateReversalBodyLineItemsItemMetadata
    """


class _SerializerTaxTransactionCreateReversalBodyLineItemsItemMetadata(
    pydantic.BaseModel
):
    """
    Serializer for TaxTransactionCreateReversalBodyLineItemsItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
