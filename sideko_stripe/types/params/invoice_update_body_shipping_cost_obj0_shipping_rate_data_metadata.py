import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata
    """


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
