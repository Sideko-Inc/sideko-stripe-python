import pydantic
import typing
import typing_extensions

from .topups_create_body_metadata_obj0 import (
    TopupsCreateBodyMetadataObj0,
    _SerializerTopupsCreateBodyMetadataObj0,
)


class TopupsCreateBody(typing_extensions.TypedDict, total=False):
    """
    TopupsCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    A positive integer representing how much to transfer.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[TopupsCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    source: typing_extensions.NotRequired[str]
    """
    The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups)).
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters.
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies this top-up as part of a group.
    """


class _SerializerTopupsCreateBody(pydantic.BaseModel):
    """
    Serializer for TopupsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerTopupsCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
