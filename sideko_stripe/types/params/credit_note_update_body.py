import pydantic
import typing
import typing_extensions

from .credit_note_update_body_metadata import (
    CreditNoteUpdateBodyMetadata,
    _SerializerCreditNoteUpdateBodyMetadata,
)


class CreditNoteUpdateBody(typing_extensions.TypedDict, total=False):
    """
    CreditNoteUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    memo: typing_extensions.NotRequired[str]
    """
    Credit note memo.
    """

    metadata: typing_extensions.NotRequired[CreditNoteUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerCreditNoteUpdateBody(pydantic.BaseModel):
    """
    Serializer for CreditNoteUpdateBody handling case conversions
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
    memo: typing.Optional[str] = pydantic.Field(alias="memo", default=None)
    metadata: typing.Optional[_SerializerCreditNoteUpdateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
