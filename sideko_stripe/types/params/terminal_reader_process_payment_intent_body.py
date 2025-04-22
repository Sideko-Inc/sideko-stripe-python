import pydantic
import typing
import typing_extensions

from .terminal_reader_process_payment_intent_body_process_config import (
    TerminalReaderProcessPaymentIntentBodyProcessConfig,
    _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfig,
)


class TerminalReaderProcessPaymentIntentBody(typing_extensions.TypedDict, total=False):
    """
    TerminalReaderProcessPaymentIntentBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    payment_intent: typing_extensions.Required[str]
    """
    PaymentIntent ID
    """

    process_config: typing_extensions.NotRequired[
        TerminalReaderProcessPaymentIntentBodyProcessConfig
    ]
    """
    Configuration overrides
    """


class _SerializerTerminalReaderProcessPaymentIntentBody(pydantic.BaseModel):
    """
    Serializer for TerminalReaderProcessPaymentIntentBody handling case conversions
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
    payment_intent: str = pydantic.Field(
        alias="payment_intent",
    )
    process_config: typing.Optional[
        _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfig
    ] = pydantic.Field(alias="process_config", default=None)
