import pydantic
import typing
import typing_extensions

from .transfer_create_body_metadata import (
    TransferCreateBodyMetadata,
    _SerializerTransferCreateBodyMetadata,
)


class TransferCreateBody(typing_extensions.TypedDict, total=False):
    """
    TransferCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    A positive integer in cents (or local equivalent) representing how much to transfer.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    destination: typing_extensions.Required[str]
    """
    The ID of a connected Stripe account. <a href="/docs/connect/separate-charges-and-transfers">See the Connect documentation</a> for details.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[TransferCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    source_transaction: typing_extensions.NotRequired[str]
    """
    You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details.
    """

    source_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_account", "card", "fpx"]
    ]
    """
    The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`.
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """


class _SerializerTransferCreateBody(pydantic.BaseModel):
    """
    Serializer for TransferCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: str = pydantic.Field(
        alias="currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    destination: str = pydantic.Field(
        alias="destination",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerTransferCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    source_transaction: typing.Optional[str] = pydantic.Field(
        alias="source_transaction", default=None
    )
    source_type: typing.Optional[
        typing_extensions.Literal["bank_account", "card", "fpx"]
    ] = pydantic.Field(alias="source_type", default=None)
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
