import pydantic
import typing
import typing_extensions

from .terminal_reader_process_payment_intent_body_process_config_tipping import (
    TerminalReaderProcessPaymentIntentBodyProcessConfigTipping,
    _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfigTipping,
)


class TerminalReaderProcessPaymentIntentBodyProcessConfig(typing_extensions.TypedDict):
    """
    Configuration overrides
    """

    allow_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]

    enable_customer_cancellation: typing_extensions.NotRequired[bool]

    skip_tipping: typing_extensions.NotRequired[bool]

    tipping: typing_extensions.NotRequired[
        TerminalReaderProcessPaymentIntentBodyProcessConfigTipping
    ]


class _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfig(
    pydantic.BaseModel
):
    """
    Serializer for TerminalReaderProcessPaymentIntentBodyProcessConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
    enable_customer_cancellation: typing.Optional[bool] = pydantic.Field(
        alias="enable_customer_cancellation", default=None
    )
    skip_tipping: typing.Optional[bool] = pydantic.Field(
        alias="skip_tipping", default=None
    )
    tipping: typing.Optional[
        _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfigTipping
    ] = pydantic.Field(alias="tipping", default=None)
