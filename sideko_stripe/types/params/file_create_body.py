import httpx
import pydantic
import typing
import typing_extensions

from .file_create_body_file_link_data import (
    FileCreateBodyFileLinkData,
    _SerializerFileCreateBodyFileLinkData,
)


class FileCreateBody(typing_extensions.TypedDict, total=False):
    """
    FileCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    file: typing_extensions.Required[httpx._types.FileTypes]
    """
    A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the `multipart/form-data` protocol.
    """

    file_link_data: typing_extensions.NotRequired[FileCreateBodyFileLinkData]
    """
    Optional parameters that automatically create a [file link](https://stripe.com/docs/api#file_links) for the newly created file.
    """

    purpose: typing_extensions.Required[
        typing_extensions.Literal[
            "account_requirement",
            "additional_verification",
            "business_icon",
            "business_logo",
            "customer_signature",
            "dispute_evidence",
            "identity_document",
            "issuing_regulatory_reporting",
            "pci_document",
            "tax_document_user_upload",
            "terminal_reader_splashscreen",
        ]
    ]
    """
    The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file.
    """


class _SerializerFileCreateBody(pydantic.BaseModel):
    """
    Serializer for FileCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    file: typing.Optional[typing.Any] = pydantic.Field(
        alias="file", default=None, exclude=True
    )
    file_link_data: typing.Optional[_SerializerFileCreateBodyFileLinkData] = (
        pydantic.Field(alias="file_link_data", default=None)
    )
    purpose: typing_extensions.Literal[
        "account_requirement",
        "additional_verification",
        "business_icon",
        "business_logo",
        "customer_signature",
        "dispute_evidence",
        "identity_document",
        "issuing_regulatory_reporting",
        "pci_document",
        "tax_document_user_upload",
        "terminal_reader_splashscreen",
    ] = pydantic.Field(
        alias="purpose",
    )

    @staticmethod
    def get_files_from_typed_dict(
        item: FileCreateBody,
    ) -> typing.List[typing.Tuple[str, httpx._types.FileTypes]]:
        files: typing.List[typing.Tuple[str, httpx._types.FileTypes]] = []

        file = item.get("file", None)
        if isinstance(file, list):
            files.extend([("file", f) for f in file])
        elif file is not None:
            files.append(("file", file))

        return files
