import pydantic
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataSepaDebit(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataSepaDebit(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
