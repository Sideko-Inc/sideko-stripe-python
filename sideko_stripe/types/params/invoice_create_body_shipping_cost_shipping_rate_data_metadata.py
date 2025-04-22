import pydantic
import typing
import typing_extensions


class InvoiceCreateBodyShippingCostShippingRateDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceCreateBodyShippingCostShippingRateDataMetadata
    """


class _SerializerInvoiceCreateBodyShippingCostShippingRateDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
