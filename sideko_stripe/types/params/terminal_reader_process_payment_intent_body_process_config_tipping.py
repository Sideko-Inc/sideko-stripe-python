import pydantic
import typing
import typing_extensions


class TerminalReaderProcessPaymentIntentBodyProcessConfigTipping(
    typing_extensions.TypedDict
):
    """
    TerminalReaderProcessPaymentIntentBodyProcessConfigTipping
    """

    amount_eligible: typing_extensions.NotRequired[int]


class _SerializerTerminalReaderProcessPaymentIntentBodyProcessConfigTipping(
    pydantic.BaseModel
):
    """
    Serializer for TerminalReaderProcessPaymentIntentBodyProcessConfigTipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_eligible: typing.Optional[int] = pydantic.Field(
        alias="amount_eligible", default=None
    )
