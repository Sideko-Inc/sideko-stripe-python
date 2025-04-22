import pydantic
import typing
import typing_extensions


class InvoiceRenderingPdf(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    page_size: typing.Optional[typing_extensions.Literal["a4", "auto", "letter"]] = (
        pydantic.Field(alias="page_size", default=None)
    )
    """
    Page size of invoice pdf. Options include a4, letter, and auto. If set to auto, page size will be switched to a4 or letter based on customer locale.
    """
