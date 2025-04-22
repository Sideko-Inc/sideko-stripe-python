import pydantic
import typing
import typing_extensions

from .source_create_body_mandate import (
    SourceCreateBodyMandate,
    _SerializerSourceCreateBodyMandate,
)
from .source_create_body_metadata import (
    SourceCreateBodyMetadata,
    _SerializerSourceCreateBodyMetadata,
)
from .source_create_body_owner import (
    SourceCreateBodyOwner,
    _SerializerSourceCreateBodyOwner,
)
from .source_create_body_receiver import (
    SourceCreateBodyReceiver,
    _SerializerSourceCreateBodyReceiver,
)
from .source_create_body_redirect import (
    SourceCreateBodyRedirect,
    _SerializerSourceCreateBodyRedirect,
)
from .source_create_body_source_order import (
    SourceCreateBodySourceOrder,
    _SerializerSourceCreateBodySourceOrder,
)


class SourceCreateBody(typing_extensions.TypedDict, total=False):
    """
    SourceCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. Not supported for `receiver` type sources, where charge amount may not be specified until funds land.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    flow: typing_extensions.NotRequired[
        typing_extensions.Literal["code_verification", "none", "receiver", "redirect"]
    ]
    """
    The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows.
    """

    mandate: typing_extensions.NotRequired[SourceCreateBodyMandate]
    """
    Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    """

    metadata: typing_extensions.NotRequired[SourceCreateBodyMetadata]

    original_source: typing_extensions.NotRequired[str]
    """
    The source to share.
    """

    owner: typing_extensions.NotRequired[SourceCreateBodyOwner]
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """

    receiver: typing_extensions.NotRequired[SourceCreateBodyReceiver]
    """
    Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`).
    """

    redirect: typing_extensions.NotRequired[SourceCreateBodyRedirect]
    """
    Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`).
    """

    source_order: typing_extensions.NotRequired[SourceCreateBodySourceOrder]
    """
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all.
    """

    token: typing_extensions.NotRequired[str]
    """
    An optional token used to create the source. When passed, token properties will override source parameters.
    """

    type_: typing_extensions.NotRequired[str]
    """
    The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Cloning card Sources](https://stripe.com/docs/sources/connect#cloning-card-sources) guide)
    """

    usage: typing_extensions.NotRequired[
        typing_extensions.Literal["reusable", "single_use"]
    ]


class _SerializerSourceCreateBody(pydantic.BaseModel):
    """
    Serializer for SourceCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    flow: typing.Optional[
        typing_extensions.Literal["code_verification", "none", "receiver", "redirect"]
    ] = pydantic.Field(alias="flow", default=None)
    mandate: typing.Optional[_SerializerSourceCreateBodyMandate] = pydantic.Field(
        alias="mandate", default=None
    )
    metadata: typing.Optional[_SerializerSourceCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    original_source: typing.Optional[str] = pydantic.Field(
        alias="original_source", default=None
    )
    owner: typing.Optional[_SerializerSourceCreateBodyOwner] = pydantic.Field(
        alias="owner", default=None
    )
    receiver: typing.Optional[_SerializerSourceCreateBodyReceiver] = pydantic.Field(
        alias="receiver", default=None
    )
    redirect: typing.Optional[_SerializerSourceCreateBodyRedirect] = pydantic.Field(
        alias="redirect", default=None
    )
    source_order: typing.Optional[_SerializerSourceCreateBodySourceOrder] = (
        pydantic.Field(alias="source_order", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    token: typing.Optional[str] = pydantic.Field(alias="token", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    usage: typing.Optional[typing_extensions.Literal["reusable", "single_use"]] = (
        pydantic.Field(alias="usage", default=None)
    )
