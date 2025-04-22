import pydantic
import typing
import typing_extensions


class TerminalReaderProcessSetupIntentBodyProcessConfig(typing_extensions.TypedDict):
    """
    Configuration overrides
    """

    enable_customer_cancellation: typing_extensions.NotRequired[bool]


class _SerializerTerminalReaderProcessSetupIntentBodyProcessConfig(pydantic.BaseModel):
    """
    Serializer for TerminalReaderProcessSetupIntentBodyProcessConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enable_customer_cancellation: typing.Optional[bool] = pydantic.Field(
        alias="enable_customer_cancellation", default=None
    )
