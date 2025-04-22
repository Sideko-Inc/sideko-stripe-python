import pydantic
import typing
import typing_extensions

from .terminal_reader_refund_payment_body_metadata import (
    TerminalReaderRefundPaymentBodyMetadata,
    _SerializerTerminalReaderRefundPaymentBodyMetadata,
)
from .terminal_reader_refund_payment_body_refund_payment_config import (
    TerminalReaderRefundPaymentBodyRefundPaymentConfig,
    _SerializerTerminalReaderRefundPaymentBodyRefundPaymentConfig,
)


class TerminalReaderRefundPaymentBody(typing_extensions.TypedDict, total=False):
    """
    TerminalReaderRefundPaymentBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    A positive integer in __cents__ representing how much of this charge to refund.
    """

    charge: typing_extensions.NotRequired[str]
    """
    ID of the Charge to refund.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[TerminalReaderRefundPaymentBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    payment_intent: typing_extensions.NotRequired[str]
    """
    ID of the PaymentIntent to refund.
    """

    refund_application_fee: typing_extensions.NotRequired[bool]
    """
    Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    """

    refund_payment_config: typing_extensions.NotRequired[
        TerminalReaderRefundPaymentBodyRefundPaymentConfig
    ]
    """
    Configuration overrides
    """

    reverse_transfer: typing_extensions.NotRequired[bool]
    """
    Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
    """


class _SerializerTerminalReaderRefundPaymentBody(pydantic.BaseModel):
    """
    Serializer for TerminalReaderRefundPaymentBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    charge: typing.Optional[str] = pydantic.Field(alias="charge", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerTerminalReaderRefundPaymentBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    payment_intent: typing.Optional[str] = pydantic.Field(
        alias="payment_intent", default=None
    )
    refund_application_fee: typing.Optional[bool] = pydantic.Field(
        alias="refund_application_fee", default=None
    )
    refund_payment_config: typing.Optional[
        _SerializerTerminalReaderRefundPaymentBodyRefundPaymentConfig
    ] = pydantic.Field(alias="refund_payment_config", default=None)
    reverse_transfer: typing.Optional[bool] = pydantic.Field(
        alias="reverse_transfer", default=None
    )
