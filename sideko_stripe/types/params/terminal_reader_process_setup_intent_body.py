import pydantic
import typing
import typing_extensions

from .terminal_reader_process_setup_intent_body_process_config import (
    TerminalReaderProcessSetupIntentBodyProcessConfig,
    _SerializerTerminalReaderProcessSetupIntentBodyProcessConfig,
)


class TerminalReaderProcessSetupIntentBody(typing_extensions.TypedDict, total=False):
    """
    TerminalReaderProcessSetupIntentBody
    """

    allow_redisplay: typing_extensions.Required[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    process_config: typing_extensions.NotRequired[
        TerminalReaderProcessSetupIntentBodyProcessConfig
    ]
    """
    Configuration overrides
    """

    setup_intent: typing_extensions.Required[str]
    """
    SetupIntent ID
    """


class _SerializerTerminalReaderProcessSetupIntentBody(pydantic.BaseModel):
    """
    Serializer for TerminalReaderProcessSetupIntentBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    allow_redisplay: typing_extensions.Literal["always", "limited", "unspecified"] = (
        pydantic.Field(
            alias="allow_redisplay",
        )
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    process_config: typing.Optional[
        _SerializerTerminalReaderProcessSetupIntentBodyProcessConfig
    ] = pydantic.Field(alias="process_config", default=None)
    setup_intent: str = pydantic.Field(
        alias="setup_intent",
    )
