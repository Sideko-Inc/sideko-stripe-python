import pydantic
import typing
import typing_extensions

from .file_link_create_body_metadata_obj0 import (
    FileLinkCreateBodyMetadataObj0,
    _SerializerFileLinkCreateBodyMetadataObj0,
)


class FileLinkCreateBody(typing_extensions.TypedDict, total=False):
    """
    FileLinkCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    The link isn't usable after this future timestamp.
    """

    file: typing_extensions.Required[str]
    """
    The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[FileLinkCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerFileLinkCreateBody(pydantic.BaseModel):
    """
    Serializer for FileLinkCreateBody handling case conversions
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
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    file: str = pydantic.Field(
        alias="file",
    )
    metadata: typing.Optional[
        typing.Union[_SerializerFileLinkCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
