import pydantic
import typing
import typing_extensions


class InvoicePreviewBodyScheduleDetailsPhasesItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemMetadata
    """


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
