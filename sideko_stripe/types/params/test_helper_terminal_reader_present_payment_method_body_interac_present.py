import pydantic
import typing
import typing_extensions


class TestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent(
    typing_extensions.TypedDict
):
    """
    Simulated data for the interac_present payment method.
    """

    number: typing_extensions.NotRequired[str]


class _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
