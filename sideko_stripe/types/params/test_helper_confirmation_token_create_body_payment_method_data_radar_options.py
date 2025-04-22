import pydantic
import typing
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataRadarOptions(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataRadarOptions(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
