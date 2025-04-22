import pydantic
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataSofort(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataSofort
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataSofort(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataSofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"] = (
        pydantic.Field(
            alias="country",
        )
    )
