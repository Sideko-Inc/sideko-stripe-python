import pydantic
import typing
import typing_extensions

from .credit_note_create_body_lines_item import (
    CreditNoteCreateBodyLinesItem,
    _SerializerCreditNoteCreateBodyLinesItem,
)
from .credit_note_create_body_metadata import (
    CreditNoteCreateBodyMetadata,
    _SerializerCreditNoteCreateBodyMetadata,
)
from .credit_note_create_body_refunds_item import (
    CreditNoteCreateBodyRefundsItem,
    _SerializerCreditNoteCreateBodyRefundsItem,
)
from .credit_note_create_body_shipping_cost import (
    CreditNoteCreateBodyShippingCost,
    _SerializerCreditNoteCreateBodyShippingCost,
)


class CreditNoteCreateBody(typing_extensions.TypedDict, total=False):
    """
    CreditNoteCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) representing the total amount of the credit note.
    """

    credit_amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
    """

    effective_at: typing_extensions.NotRequired[int]
    """
    The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
    """

    email_type: typing_extensions.NotRequired[
        typing_extensions.Literal["credit_note", "none"]
    ]
    """
    Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice: typing_extensions.Required[str]
    """
    ID of the invoice.
    """

    lines: typing_extensions.NotRequired[typing.List[CreditNoteCreateBodyLinesItem]]
    """
    Line items that make up the credit note.
    """

    memo: typing_extensions.NotRequired[str]
    """
    The credit note's memo appears on the credit note PDF.
    """

    metadata: typing_extensions.NotRequired[CreditNoteCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    out_of_band_amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
    """

    reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
        ]
    ]
    """
    Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
    """

    refund_amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
    """

    refunds: typing_extensions.NotRequired[typing.List[CreditNoteCreateBodyRefundsItem]]
    """
    Refunds to link to this credit note.
    """

    shipping_cost: typing_extensions.NotRequired[CreditNoteCreateBodyShippingCost]
    """
    When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
    """


class _SerializerCreditNoteCreateBody(pydantic.BaseModel):
    """
    Serializer for CreditNoteCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    credit_amount: typing.Optional[int] = pydantic.Field(
        alias="credit_amount", default=None
    )
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    email_type: typing.Optional[typing_extensions.Literal["credit_note", "none"]] = (
        pydantic.Field(alias="email_type", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice: str = pydantic.Field(
        alias="invoice",
    )
    lines: typing.Optional[typing.List[_SerializerCreditNoteCreateBodyLinesItem]] = (
        pydantic.Field(alias="lines", default=None)
    )
    memo: typing.Optional[str] = pydantic.Field(alias="memo", default=None)
    metadata: typing.Optional[_SerializerCreditNoteCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    out_of_band_amount: typing.Optional[int] = pydantic.Field(
        alias="out_of_band_amount", default=None
    )
    reason: typing.Optional[
        typing_extensions.Literal[
            "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
        ]
    ] = pydantic.Field(alias="reason", default=None)
    refund_amount: typing.Optional[int] = pydantic.Field(
        alias="refund_amount", default=None
    )
    refunds: typing.Optional[
        typing.List[_SerializerCreditNoteCreateBodyRefundsItem]
    ] = pydantic.Field(alias="refunds", default=None)
    shipping_cost: typing.Optional[_SerializerCreditNoteCreateBodyShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
