import pydantic
import typing
import typing_extensions


class InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata
    """


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
