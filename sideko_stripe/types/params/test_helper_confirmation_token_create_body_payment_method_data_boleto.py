import pydantic
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataBoleto(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataBoleto(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
