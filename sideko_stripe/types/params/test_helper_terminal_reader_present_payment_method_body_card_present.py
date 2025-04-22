import pydantic
import typing
import typing_extensions


class TestHelperTerminalReaderPresentPaymentMethodBodyCardPresent(
    typing_extensions.TypedDict
):
    """
    Simulated data for the card_present payment method.
    """

    number: typing_extensions.NotRequired[str]


class _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyCardPresent(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTerminalReaderPresentPaymentMethodBodyCardPresent handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
