import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file_links import FileLinks


class File(pydantic.BaseModel):
    """
    This object represents files hosted on Stripe's servers. You can upload
    files with the [create file](https://stripe.com/docs/api#create_file) request
    (for example, when uploading dispute evidence). Stripe also
    creates files independently (for example, the results of a [Sigma scheduled
    query](#scheduled_queries)).

    Related guide: [File upload guide](https://stripe.com/docs/file-upload)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The file expires and isn't available at this time in epoch seconds.
    """
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    """
    The suitable name for saving the file to a filesystem.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    links: typing.Optional["FileLinks"] = pydantic.Field(alias="links", default=None)
    """
    A list of [file links](https://stripe.com/docs/api#file_links) that point at this file.
    """
    object: typing_extensions.Literal["file"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    purpose: typing_extensions.Literal[
        "account_requirement",
        "additional_verification",
        "business_icon",
        "business_logo",
        "customer_signature",
        "dispute_evidence",
        "document_provider_identity_document",
        "finance_report_run",
        "financial_account_statement",
        "identity_document",
        "identity_document_downloadable",
        "issuing_regulatory_reporting",
        "pci_document",
        "selfie",
        "sigma_scheduled_query",
        "tax_document_user_upload",
        "terminal_reader_splashscreen",
    ] = pydantic.Field(
        alias="purpose",
    )
    """
    The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file.
    """
    size: int = pydantic.Field(
        alias="size",
    )
    """
    The size of the file object in bytes.
    """
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    """
    A suitable title for the document.
    """
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    """
    The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`).
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    Use your live secret API key to download the file from this URL.
    """
