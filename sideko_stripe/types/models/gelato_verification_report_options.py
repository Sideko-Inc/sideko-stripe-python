import pydantic
import typing

from .gelato_report_document_options import GelatoReportDocumentOptions


class GelatoVerificationReportOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document: typing.Optional[GelatoReportDocumentOptions] = pydantic.Field(
        alias="document", default=None
    )
    id_number: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="id_number", default=None
    )
